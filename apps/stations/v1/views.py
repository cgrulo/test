# coding: utf8
from urbvan_framework.views import ListCreateView, ListUpdateView
from .schemas import LocationSchema
from .serializers import LocationSerializer, LocationSerializerUpdate
from ..models import LocationModel
from rest_framework import generics, mixins
from urbvan_framework.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class LocationView(ListUpdateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializerUpdate


class LocationCrudView(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):

    #lookup_field = 'id'
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializerUpdate
    schema_class = LocationSchema

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)


    def get_queryset(self):
        return LocationModel.objects.all()

    def get_serializer_context(self):
        return{'request': self.request}

