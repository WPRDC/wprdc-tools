from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<guide_id>[\w-]+)/$', views.guide),
    url(r'^(?P<guide_id>[\w-]+)/(?P<dataset_id>[\w-]+)/$', views.dataset),
]