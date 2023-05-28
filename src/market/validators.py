from marshmallow import Schema, fields, validate, validates_schema, ValidationError

from database.models import Product, Category


class ProductCreateValidater(Schema):
    name = fields.String(required=True, validate=validate.Length(max=255))
    description = fields.String(required=False, missing=None, load_only=True)
    price = fields.String(required=True)
    category_id = fields.Integer()

    @validates_schema
    def valideter_name(self, data, **kwargs):
        name = data.get('name', None)
        product = Product.query.filter(Product.name == name).first()
        if product:
            raise ValidationError('This is name is bory')
    
    @validates_schema
    def validater_price(self, data, **kwargs):
        price = data.get('price', None)
        if not price or not price.isdigit() or int(price[0]) < 1:
            raise ValidationError('Error price value')

    @validates_schema
    def validater_category_id(self, data, **kwargs):
        category_id = data.get('category_id', None)
        category = Category.query.filter(Category.id == category_id).first()
        if not category:
            raise ValidationError('This category ID not found')