from marshmallow import Schema, fields
import uuid


class CreateUserRequest(Schema):
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    othernames = fields.Int(required=False)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=True)
