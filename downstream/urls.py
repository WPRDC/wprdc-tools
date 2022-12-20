from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^(?P<resource_id>[^/]+)$', views.stream_response, name='stream_response'),
    re_path('^(?P<resource_id>[^/]+)/(?P<file_format>[^/]+)$', views.stream_response, name='stream_by_file_format'),
]
