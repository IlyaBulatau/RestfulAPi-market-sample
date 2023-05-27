import sqlalchemy as db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from database.connect import Base

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email = db.Column(db.String(lenght=255),unique=True, nullable=False)
    location = db.Column(db.String(length=255), nullable=True)
    password = db.Column(db.String(), nullable=False)
    products = relationship('Product', backref='user')

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.location = kwargs.get('location', None)
        self.password = generate_password_hash(kwargs.get('password'), method='sha256')
    
    def get_token(self):
        token = ...
        return token


class Category(Base):
    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True)
    products = relationship('Product', backref='category')


class Product(Base):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(lenght=255), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    price = db.Column(db.String(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
