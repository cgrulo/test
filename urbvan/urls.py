# coding: utf8
from django.contrib import admin
from django.urls import (include, path)
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/api/', include('apps.stations.urls', namespace='api')),
    path('v1/api2/', include('apps.lines.urls', namespace='api2')),
]
