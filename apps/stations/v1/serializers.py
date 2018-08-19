# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel
from apps.stations.models import Profile


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class LocationSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        fields = '__all__'

        def validate_id(self):
            if self.request.method == 'PUT' or self.request.method == 'PATCH':

