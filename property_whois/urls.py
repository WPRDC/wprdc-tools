from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^whois/$', views.get_owner),
    url(r'^whois/(?P<parcel_id>[\w-]+)/$', views.get_owner),
]
