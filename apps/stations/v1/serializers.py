# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class LocationSerializerCRUD(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        fields = [
            'id',
            'name',
            'latitude',
            'longitude',
        ]

        read_only_fields = ['id',]

    # Convertir a JSON
    # Validacion para datos pasados nombre no se repita


    def validate_name(self, value):
        qs = LocationModel.objects.filter(name__iexact=value)

        #excluye de la seleccion al mismo objeto
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError('Ya existe un location con este nombre')

        return value


