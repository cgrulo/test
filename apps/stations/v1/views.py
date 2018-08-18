# coding: utf8
from urbvan_framework.views import ListCreateView
from .schemas import LocationSchema
from .serializers import LocationSerializer, LocationSerializerCRUD
from ..models import LocationModel
from rest_framework import generics
from urbvan_framework.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.users.models import Profile

class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationCrudView(generics.ListAPIView):

    lookup_field = 'pk'
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializerCRUD


    def get_queryset(self):
        return LocationModel.objects.all()

    def get_serializer_context(self):
        return{'request': self.request}
