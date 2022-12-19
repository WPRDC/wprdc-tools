from django.shortcuts import render
from django.http import  JsonResponse

from .utils import get_owner_name

# Create your views here.
def index(request):
    return render(request, 'property_whois/index.html')


def get_owner(request, parcel_id=''):
    print(parcel_id)
    owner_name = get_owner_name(parcel_id)
    return JsonResponse({'name': get_owner_name(parcel_id), 'success': bool(owner_name)})

