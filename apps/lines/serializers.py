from rest_framework import serializers
from .models import  LineModel, StationModel
from apps.users.models import Profile
from apps.stations.v1.serializers import StationsUpdateSerializer
class LineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        exclude = (
            'id',
        )
        # fields ='__all__'

    def validate_name(self, value):
        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo == 'usuario' or tipo == 'urbvan':
            raise serializers.ValidationError('No tiene los permisos')
        else:
            return value

        read_only_fields = ['id', ]
class LineUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields ='__all__'
        read_only_fields =['id',]

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

class RouteCreateSerializer(serializers.ModelSerializer, serializers.Serializer):
    class Meta:
        model = StationModel
        exclude = (
            'id',
        )
        stations = StationsUpdateSerializer()

    def validate_direction(self, value):
        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo == 'usuario' or tipo == 'urbvan':
            raise serializers.ValidationError('No tiene los permisos')
        else:
            return value

class RouteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationModel
        fields = '__all__'
        read_only_fields = ['id', ]
        stations = StationsUpdateSerializer()

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


