# coding: utf8
from rest_framework import serializers

from ..models import LocationModel, StationModel
from apps.users.models import Profile


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )




class LocationSerializerUpdate(serializers.ModelSerializer):

    #El serializer para el update de locations, valida si el perfil de usuario es "usuario"
    #y le niega el poder continuar, para los otros 2 tipos de usuarios (admin y urbvan) se tiene permitido
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

    #Para creat stations tambien se valida el tipo de usuario en este caso para crear los nuevos stations
    #solo lo puede hacer el admin

    class Meta:
        model = StationModel
        exclude = ('id',)

    def validate_is_active(self, value):
        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo =='usuario' or tipo == 'urbvan':
            raise serializers.ValidationError('No tiene los permisos')
        else:
            return value


class StationsUpdateSerializer(serializers.ModelSerializer):
    #Los updates estan permitidos para usuarios "admin" y "urbvan"
    class Meta:
        model = StationModel
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