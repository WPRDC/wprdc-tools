from django.urls import re_path

from . import views

urlpatterns = [
    #===================================================================================================================
    # Alpha
    #===================================================================================================================
    re_path(r'^$', views.index, name='index'),
    re_path(r'^single/$', views.single, name='single'),
    re_path(r'^beta/single/$', views.single, name='beta-single'),
    re_path(r'^batch/$', views.batch, name='batch'),
    re_path(r'^within/$', views.within, name='within'),
    re_path(r'^data_within/$', views.data_within, name='data_within'),
    re_path(r'^progress/$', views.get_progress, name='get_progress'),
    re_path(r'^get_collected_data/$', views.get_collected_data, name='get_collected_data'),

    #===================================================================================================================
    # Beta
    # ===================================================================================================================
    re_path(r'^beta/parcels/(?P<parcel_ids>[\w,]*)$', views.beta_parcels, name='single_parcel'),
    re_path(r'^v1/parcels/(?P<parcel_ids>[\w,]*)$', views.beta_parcels, name='single_parcel'),
    re_path(r'^v0/parcels/(?P<parcel_ids>[\w,]*)$', views.beta_parcels, name='single_parcel'),

    # These calls work as part of one big async system
    # data-within requests data within a region,
    re_path(r'^v0/data_within/$', views.data_within, name='data_within'),
    #  progress returns how far that process is
    re_path(r'^v0/progress/$', views.get_progress, name='get_progress'),
    # get_collected_data gets that data collected through the aysnc data-within method
    re_path(r'^v0/get_collected_data/$', views.get_collected_data, name='get_collected_data'),



]