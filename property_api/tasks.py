from __future__ import absolute_import

import time
from collections import defaultdict

from .models import CKANResource
from .utils import chunks, get_batch_data, carto_intersect, intersect

from tools.celery import app
from celery import current_task
import json

def log(fname, info):
    with open(fname, 'w') as f:
        f.write(json.dumps(info, indent=2))


def update_progress(task, percent):
    print(task, percent)
    current_task.update_state(state='PROGRESS', meta={'task': task, 'percent': percent})
    


@app.task
def async_data_in_shape(shape, fields):
    print('start', time.clock())
    update_progress('starting', 0)
    data, failed_searches = {}, []
    resources = CKANResource.objects.filter(resource_id__in=fields.keys())
    all_fields = []

    # Get PINs
    update_progress('Gathering Parcels from Your Region', 10)
    status, pins, geos = intersect(shape)
    print('CHECKING PINS')
    for pin in pins:
        if pin not in geos.keys():
            print('{} not found!'.format(pin))
    # Get data for the parcels
    num = len(resources) if len(resources) else 1
    log('/home/sds25/pins.log', pins)
    cntr = 50 + (30 //num)
    for resource in resources:
        data[resource.slug] = {}
        success = False
        update_progress('Gathering {} Data'.format(resource.name), cntr)
        cntr += (30 // num)
        for pin_list in chunks(pins, 100):
            success, temp_data, fieldset = get_batch_data(pin_list, resource,
                                                          fields=fields[str(resource.resource_id)], clean=True)

            data[resource.slug].update(temp_data)

            if success:
                print('pulled {} data'.format(resource.name), time.clock())

                for field in fieldset:
                    if field not in all_fields:
                        all_fields.append(field)

        if not success:
            print('failed search')
            failed_searches.append(resource.name)

    # Pivot data to be per parcel, not resource
    update_progress('Pivoting Data', 90)
    pin_data = defaultdict(dict)
    log('/home/sds25/data.log', data)
    log('/home/sds25/geos.log', geos)
    for resource_key, resource_data in data.items():
        resource = CKANResource.objects.get(pk=resource_key)
        pin_field = resource.parcel_id_field
        bad_count = 0;

        for parcel_key, parcel_data in resource_data.items():
            if pin_field in parcel_data:
                del parcel_data[pin_field]

            pin_data[parcel_key][resource_key] = parcel_data

            if 'geo' not in pin_data[parcel_key]:
                pin_data[parcel_key]['geo'] = geos[parcel_key]
                
        print("BAD: {}".format(bad_count))

    print('pivoted data', time.clock())
    print('all_fields: ', all_fields)


    update_progress('Generating Download', 95)
    return pin_data, all_fields
