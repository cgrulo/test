# coding: utf8
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .mixins import (CreateModelMixin, ListModelMixin, UpdateModelMixin)
from .schemas import PaginationResponse
#from rest_framework.authentication import TokenAuthentication
from .authentication import CustomTokenAuthentication


class CreateAPIView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
    """
    Concrete view for listing a queryset.
    """

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    pagination_class = PaginationResponse

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateApiView(UpdateModelMixin, GenericAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # def put(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class ListCreateView(CreateAPIView, ListAPIView):
    pass

class ListUpdateView(UpdateApiView, ListAPIView):
    pass