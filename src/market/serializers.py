from marshmallow import Schema, fields


class CategoryDetailSerialier(Schema):

    class Meta:
        ordered = True

    id = fields.Integer()
    name = fields.String()


class UserDetailSerialier(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String(required=False, missing=None)
    location = fields.String(required=False, missing=None)
    password = fields.String(load_only=True)


class ProductDetailSerializer(Schema):

    id = fields.Integer()
    name = fields.String()
    description = fields.String(required=False, missing=None)
    price = fields.String()
    category_id = fields.Integer(load_only=True)
    user_id = fields.Integer(load_only=True)
    category = fields.Nested(CategoryDetailSerialier)
    user = fields.Nested(UserDetailSerialier)

    class Meta:
        ordered = True
