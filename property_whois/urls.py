from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^whois/$', views.get_owner),
    re_path(r'^whois/(?P<parcel_id>[\w-]+)/$', views.get_owner),
]
