from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from urbvan_framework.authentication import CustomTokenAuthentication
from urbvan_framework.views import ListCreateView, UpdateApiView
from .models import LineModel, RouteModel
from .serializers import LineCreateSerializer,LineUpdateSerializer, RouteCreateSerializer, RouteUpdateSerializer
from .schemas import LinecreateSchema, RouteCreateSchema


class LineModelCreateView(ListCreateView):

    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LineModel.objects.all()
    serializer_class = LineCreateSerializer
    schema_class = LinecreateSchema

    # def perform_create(self, serializer):
    #     serializer.save()


class LineModelUpdateView(generics.RetrieveUpdateAPIView):

    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LineModel.objects.all()
    serializer_class = LineUpdateSerializer


class LineModelDeleteView(generics.DestroyAPIView):

    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = LineModel.objects.all()

class RouteModelCreateView(generics.ListCreateAPIView):

    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = RouteModel.objects.all()
    serializer_class = RouteCreateSerializer
    schema_class = RouteCreateSchema

class RouteModelUpdateView(UpdateApiView):

    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = RouteModel.objects.all()
    serializer_class = RouteUpdateSerializer

class RouteModelDeleteView(generics.DestroyAPIView):

    lookup_field = 'id'
    ordering = ['-id']
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = RouteModel.objects.all()
