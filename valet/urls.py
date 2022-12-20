from django.urls import path

from . import views

urlpatterns = [
    path('ajax/get_dates/ ', views.get_dates, name='get_dates'),
    path('ajax/get_features/ ', views.get_features, name='get_features'),
    path('ajax/get_results/ ', views.get_results, name='get_results'),
    path('public/ ', views.public, name='public'),
    path('nonpublic/ ', views.nonpublic, name='nonpublic'),
    path('login/ ', views.nonpublic, name='force_login'),
    path('logout/ ', views.logout_view, name='logout'),
    path('logff/ ', views.logout_view, name='logout'),
    path('', views.index, name='index'),
]
