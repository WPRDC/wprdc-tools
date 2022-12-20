from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<resource_id>.*)/(?P<field>.*)/(?P<search_term>.*)/csv$', views.csv_view, name='show_csv'),
    re_path(r'^(?P<resource_id>.*)/(?P<field>.*)/(?P<search_term>.*)$', views.results, name='results'),
]
