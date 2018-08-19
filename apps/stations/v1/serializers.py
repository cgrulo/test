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

    def validate_id(self, value):
        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo =='usuario':
            raise serializers.ValidationError('No tiene los permisos')
        else:
            return value


class LocationSerializerDelete(serializers.ModelSerializer):

    class Meta:

        model = LocationModel
        fields = (
            'id',
            'name',
        )

    def validate_id(self, value):

        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo == 'usuario':
            raise serializers.ValidationError('No tiene los permisos')
        else:
            return value