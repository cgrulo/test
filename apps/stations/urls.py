# coding: utf8
from django.urls import path

from .v1.views import LocationCrudView, LocationView, LocationDelete
from .v1.views import StationsDeleteView, StationsListCreateView, StationsUpdateView
app_name = 'stations'
urlpatterns = [
    path('locations/update/<id>/', LocationCrudView.as_view(), name='v1_update_location'),
    path('locations/delete/<id>/', LocationDelete.as_view(), name='v1_delete_location'),
    path('locations/', LocationView.as_view(), name='v1_list_create_location'),
    path('stations/update/<id>/', StationsUpdateView.as_view(), name='v1_update_station'),
    path('stations/delete/<id>/', StationsDeleteView.as_view(), name='v1_delete_station'),
    path('stations/', StationsListCreateView.as_view(), name='v1_list_station'),
]
