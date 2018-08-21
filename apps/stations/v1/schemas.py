# coding: utf8
from marshmallow import (Schema, fields, validates_schema, ValidationError)
from apps.users.models import Profile

#Se hace la serializacion por medio de marshmallow
class LocationSchema(Schema):


    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()

    #Se valido el codigo pero en este caso no pude hacer que funcionara
    # con los metodos que implementaron, pero hace que solo el perfil admin
    # pueda crear Locations
    @validates_schema
    def validate_name(self, data):
        request = self.context.get("request")
        user = request.user
        profiles = Profile.objects.filter(user__id=user.id)
        for profile in profiles:
            tipo = profile.tipo

        if tipo =='usuario' or tipo =='urbvan':
            raise ValidationError('No cuentas con los permisos para la operacion')

        else:
            return data

class StationSchema(Schema):

    id = fields.String()
    location = fields.Nested(LocationSchema)
    order = fields.Integer()
    is_active = fields.Boolean()
