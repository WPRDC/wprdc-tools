from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

import json
from collections import OrderedDict as OD

from .models import Guide, DataSet, PubliclyAvailableData, NotPubliclyAvailableData, WhereToFind, ThingsToKnow, Tool


# Create your views here.
def index(request):
    '''
    LibGuide general landing page.  Lists available Lib guides

    :param request:
    :return:
    '''
    guides = Guide.objects.filter(display=True)
    return render(request, 'lib-guides/index.html', {'guides': guides})


def guide(request, guide_id=''):
    guide = get_object_or_404(Guide, pk=guide_id)
    if not guide.display:
        return HttpResponseNotFound
    tools = Tool.objects.filter(guide=guide_id)
    datasets = DataSet.objects.filter(guide=guide_id)


    return render(request, 'lib-guides/guide.html', {'guide': guide, 'tools': tools, 'datasets': datasets})

def dataset(request, guide_id='', dataset_id=''):
    guide = get_object_or_404(Guide, pk=guide_id)
    if not guide.display:
        return HttpResponseNotFound
    _dataset = get_object_or_404(DataSet, pk=dataset_id)

    return render(request, 'lib-guides/dataset.html', {'guide': guide, 'dataset':_dataset})