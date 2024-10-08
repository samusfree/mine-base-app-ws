from flask_marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    born = fields.Date(required=True)
