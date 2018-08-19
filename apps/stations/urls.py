# coding: utf8
from django.urls import path

from .v1.views import LocationCrudView, LocationView, LocationDelete

app_name = 'stations'
urlpatterns = [
    path('update/<id>/', LocationCrudView.as_view(), name='v1_update_location'),
    path('delete/<id>/', LocationDelete.as_view(), name='v1_delete_location'),
    path('', LocationView.as_view(), name='v1_list_location'),


]
