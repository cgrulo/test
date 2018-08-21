from marshmallow import (Schema, fields, validates_schema, ValidationError)
from apps.stations.v1.schemas import StationSchema

class LinecreateSchema(Schema):
    id = fields.String()
    name = fields.String()
    color = fields.String()

class RouteCreateSchema(Schema):
    id = fields.String()
    line = fields.Nested(LinecreateSchema)
    stations = fields.Nested(StationSchema, many=True, dump_only=True)
    direction = fields.Boolean()
    is_active = fields.Boolean()
