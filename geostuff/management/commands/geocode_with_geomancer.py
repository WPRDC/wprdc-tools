"""This is an older version of the script."""
import requests, csv, sys, time, os
from pprint import pprint

from geostuff.util import forward_geocode

from django.conf import settings
from django.core.management.base import BaseCommand

def write_to_csv(filename, list_of_dicts, keys):
    # Stolen from parking-data util.py file.
    with open(filename, 'w') as g:
        g.write(','.join(keys)+'\n')
    with open(filename, 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, extrasaction='ignore', lineterminator='\n')
        #dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)

def write_or_append_to_csv(filename, list_of_dicts, keys):
    if not os.path.isfile(filename):
        with open(filename, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, extrasaction='ignore', lineterminator='\n')
            dict_writer.writeheader()
    with open(filename, 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, extrasaction='ignore', lineterminator='\n')
        dict_writer.writerows(list_of_dicts)

def form_full_address(row):
    maybe_malformed = False
    if 'STREET_ADDRESS' in row:
        street_address = row['STREET_ADDRESS']
    elif 'ADD_LINE_1' in row:
        street_address = row['ADD_LINE_1']
        if 'ADD_LINE_2' in row and row['ADD_LINE_2'] != '':
            if street_address == '':
                street_address = row['ADD_LINE_2']
                maybe_malformed = True
            else:
                street_address += ', ' + row['ADD_LINE_2']
    #if row['CITY'] == '':

    return "{}, {}, {} {}".format(street_address, row['CITY'], row['STATE'], row['ZIP'])

def form_full_asset_address(row):
    maybe_malformed = False
    if 'state' in row:
        state= row['state']
    else:
        state = 'PA'

    return "{}, {}, {} {}".format(row['street_address'], row['city'], state, row['zip_code'])

class Command(BaseCommand):
    help = 'Dump assets to a CSV file, with the option to specify one or more asset types as command-line arguments.\n\nUsage:\n> python manage.py dump_assets_by_type <asset_type>'

    def add_arguments(self, parser): # Necessary boilerplate for accessing args.
        parser.add_argument('args', nargs='*')

    def handle(self, *args, **options):
        test = False
        if test:
            # geocode - takes address, city, state, country in any form, raises exception if can't parse address
            geocoded = geocode('3343 Forbes Ave, Pittsburgh, PA')
            pprint(geocoded)
        else:
            print("args = {}".format(args))
            if len(args) < 1:
                raise ValueError("Please specify the filename as the 1st command-line argument.")
        
            filepath = args[0]
            print(filepath)
            pathparts = filepath.split('/')
            pathparts[-1] = 'geocoded-'+pathparts[-1]
            output_filepath = '/'.join(pathparts)
            print("output_filepath = {}".format(output_filepath))
            reader = csv.DictReader(open(filepath))
        
            headers = reader.fieldnames
            headers += ['latitude', 'longitude', 'full_address', 'geom_type', 'census_tract', 'allegheny_county_municipality', 'geocoding_status']
            print(headers)
        
            rows = []
            for k, row in enumerate(reader):
                if False:
                    full_address = form_full_address(row)
                else: # Assume asset-dump format here
                    full_address = form_full_asset_address(row)
                    row['full_address'] = full_address
                
                result = forward_geocode(full_address, disambiguate=True) # Pass the whole string
                row['geocoding_status'] = result['status']
                row['geocoding_properties'] = 'Geocoded by Geomancer'
                if result['status'] not in ['ERROR', 'Unable to geocode this address to a single unambigous point.']:
                    row['geom_type'] = result['geom']['type'] 
                    row['latitude'] = result['geom']['coordinates'][1]
                    row['longitude'] = result['geom']['coordinates'][0]
                    row['census_tract'] = result['regions']['us_census_tract']['name'] if 'us_census_tract' in result['regions'] else ''
                    row['allegheny_county_municipality'] = result['regions']['allegheny_county_municipality']['name'] if 'allegheny_county_municipality' in result['regions'] else ''
        
                    #if first_feature['properties']['name'] == 'Clinton County' and first_feature['properties']['confidence'] < 0.5 and row['CITY'] == 'Clinton':
                    #    row['CITY'] = 'Findlay Township'
                    #    full_address = form_full_address(row)
                    #    row['full_address'] = full_address
                    #    try:
                    #        geocoding_response = gisAPI.geocode(full_address)
                    #        features = geocoding_response['features']
                    #        first_feature = features[0]
                    #    except Exception as e:
                    #        if full_address[:3] != ', ,':
                    #            print(f"Unable to parse {full_address}")
                    #        row['error'] = 'Unable to parse address'
                            
        
                rows.append(row)
                time.sleep(0.01)
                if k % 1000 == 0:
                    print("On record {}".format(k))
                    write_or_append_to_csv(output_filepath, rows, headers)
                    rows = []

            write_or_append_to_csv(output_filepath, rows, headers)
