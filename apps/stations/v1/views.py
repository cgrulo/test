# coding: utf8
from urbvan_framework.views import ListCreateView, ListUpdateView, ListView
from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, LocationSerializerUpdate, LocationSerializerDelete
from .serializers import StationsListCreateSerializer, StationsUpdateSerializer
from ..models import LocationModel, StationModel
from rest_framework import generics, mixins
from urbvan_framework.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from rest_framework import status
# from rest_framework.response import Response

#--- ordering se usa para ordenar los datos.

class LocationCrudView(ListUpdateView):
    lookup_field = 'id'
    ordering = ['-id']
    queryset = LocationModel.objects.all()
    # schema_class = LocationSchema
    serializer_class = LocationSerializerUpdate

class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    ordering = ['-id']

class LocationDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializerDelete

    #---- Se intento sobrecargar el metodo destroy para hacer la validacion----


    # def perform_destroy(self, instance):

    # def destroy(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     request = self.context.get("request")
    #     user = request.user
    #     profiles = Profile.objects.filter(user__id=user.id)
    #     for profile in profiles:
    #         tipo = profile.tipo
    #
    #     if tipo == 'usuario':
    #         return
    #     else:
    #         if obj.survey:
    #             return Response(data={'message': "Too late to delete"},
    #                             status=status.HTTP_400_BAD_REQUEST)
    #         self.perform_destroy(obj)
    #         return Response(status=status.HTTP_204_NO_CONTENT)


class StationsListCreateView(ListCreateView):
    #--- Se uso la vista dentro de urbvan_framework ----
    queryset = StationModel.objects.all()
    ordering = ['-id']
    schema_class = StationSchema
    serializer_class = StationsListCreateSerializer


#Se usaron vistas genericas para la creacion de las otras views para station

class StationsUpdateView(generics.RetrieveUpdateAPIView):


    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = StationModel.objects.all()
    serializer_class = StationsUpdateSerializer

class StationsDeleteView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = StationModel.objects.all()
