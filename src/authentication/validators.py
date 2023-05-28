from marshmallow import Schema, fields, validate, validates_schema, ValidationError

from database.models import User

class RegisterShemaValidator(Schema):
    username = fields.String(required=True, validate=[validate.Length(min=3, max=30)])
    email = fields.String(validate=[validate.Email()])
    location = fields.String(required=False, missing=None)
    password = fields.String()

    @validates_schema
    def validate_username(self, data, **kwargs):
        username = data.get('username', None)
        user = User.query.filter(User.username == username).first()
        if user:
            raise ValidationError('This is username is busy')

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get('email', None)
        user = User.query.filter(User.email == email).first()
        if user:
            raise ValidationError('This is email is busy')
        
 

