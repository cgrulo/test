# coding: utf8
from marshmallow import (Schema, fields, validates_schema, ValidationError)
from apps.users.models import Profile


class LocationSchema(Schema):


    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()

    @validates_schema
    def validate_name(self, data):
        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo =='usuario':
            raise ValidationError('No cuentas con los permisos para la operacion')

        else:
            return data

class StationSchema(Schema):

    id = fields.String()
    location = fields.Nested(LocationSchema)
    order = fields.Integer()
    is_active = fields.Boolean()
