# coding: utf8
from urbvan_framework.views import ListCreateView, ListUpdateView, ListView
from .schemas import LocationSchema
from .serializers import LocationSerializer, LocationSerializerUpdate, LocationSerializerDelete
from ..models import LocationModel
from rest_framework import generics, mixins
from urbvan_framework.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.stations.models import Profile
from rest_framework import status
from rest_framework.response import Response


class LocationCrudView(ListUpdateView):
    lookup_field = 'id'
    queryset = LocationModel.objects.all()
    # schema_class = LocationSchema
    serializer_class = LocationSerializerUpdate

class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class LocationDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializerDelete

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




# class LocationCrudView(ListUpdateView):
#
#     #lookup_field = 'id'
#     authentication_classes = (CustomTokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     serializer_class = LocationSerializerUpdate
#     schema_class = LocationSchema
#
#     def perform_create(self, serializer):
#         current_user = self.request.user
#         serializer.save(user=current_user)
#
#
#     def get_queryset(self):
#         return LocationModel.objects.all()
#
#     def get_serializer_context(self):
#         return{'request': self.request}

