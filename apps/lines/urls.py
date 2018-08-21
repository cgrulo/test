from django.urls import path

from .views import LineModelCreateView, LineModelUpdateView, LineModelDeleteView, RouteModelCreateView
from .views import RouteModelUpdateView, RouteModelDeleteView
app_name = 'lines'

urlpatterns = [
    path('lines/', LineModelCreateView.as_view(), name='lines_create'),
    path('lines/update/<id>/', LineModelUpdateView.as_view(), name='lines_update'),
    path('lines/delete/<id>/', LineModelDeleteView.as_view(), name='lines_delete'),
    path('routes/', RouteModelCreateView.as_view(), name='routes_create'),
    path('routes/update/<id>/', RouteModelUpdateView.as_view(), name='routes_update'),
    path('routes/delete/<id>/', RouteModelDeleteView.as_view(), name='routes_delete'),

]