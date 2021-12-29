from marshmallow import Schema, fields


class CreateHomeRequest(Schema):
    name = fields.Str(required=True)
    authorId = fields.Str(required=True)
    price = fields.Int(required=True)
    address = fields.Str(required=True)
    sqrFtSize = fields.Str(required=True)
    description = fields.Str(required=True)
