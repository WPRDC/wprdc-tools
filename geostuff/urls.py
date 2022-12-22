from django.urls import re_path

from . import views

# REGEX FOR COORDINATE STRING: (?P<coord_string>(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?))


api_urls = [
    re_path(r'^api/v0/parcels_in/(?P<region_type>[\w-]+)/(?P<region_name>[\w-]+)/$', views.parcels_in, name='v0_parcels_in'),
    re_path(r'^api/v0/spatial-query/(?P<region_type>[\w-]+)/(?P<region_name>[\w-]+)/$', views.spatial_query_object, name='v0_intersect'),
    re_path(r'^api/v0/regions/$', views.region_types, name='v0_regions_types'),
    re_path(r'^api/v0/regions/(?P<region_type>[\w-]+)/$', views.regions, name='v0_regions'),
    re_path(r'^api/v0/reverse_geocode/$', views.reverse_geocode, name='v0_reverse_geocode'),
    re_path(r'^api/v0/geocode/$', views.geocode, name='v0_geocode'),
]

urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    re_path(r'^parcels_in/(?P<region_type>[\w-]+)/(?P<region_name>[\w-]+)/$', views.parcels_in_old, name='parcels_in_old'),
    re_path(r'^api/spatial-query/(?P<region_type>[\w-]+)/(?P<region_name>[\w-]+)/$', views.spatial_query_object, name='v0_intersect'),

    re_path(r'^regions/$', views.region_types, name='regions_types'),
    re_path(r'^regions/(?P<region_type>[\w-]+)/$', views.regions, name='regions'),

    re_path(r'^reverse_geocode/$', views.reverse_geocode, name='reverse_geocode'),
    re_path(r'^geocode/$', views.geocode, name='geocode'),
    re_path(r'^address_search/$', views.address_search, name='addr_search'),

    re_path(r'^upload/$', views.upload_file, name="file_upload")
] + api_urls
