# coding: utf8
from rest_framework import serializers

from ..models import LocationModel, StationModel
from apps.users.models import Profile


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

    # def validate_id(self, value):
    #
    #     request = self.context.get("request")
    #     user = request.user
    #     profiles = Profile.objects.filter(user__id=user.id)
    #     for profile in profiles:
    #         tipo = profile.tipo
    #
    #     if tipo == 'usuario':
    #         raise serializers.ValidationError('No tiene los permisos')
    #     else:
    #         return value

class StationsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationModel
        exclude = ('id',)



class StationsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationModel
        fields = '__all__'