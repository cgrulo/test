# coding: utf8
from django.urls import path

from .v1 import views as views_v1

app_name = 'stations'
urlpatterns = [

    path('', views_v1.LocationView.as_view(), name='v1_list_create_location'),
]
