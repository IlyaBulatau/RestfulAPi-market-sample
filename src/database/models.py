import sqlalchemy as db
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token

from database.connect import Base, session

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email = db.Column(db.String(length=255),unique=True, nullable=False)
    location = db.Column(db.String(length=255), nullable=True)
    password = db.Column(db.String(), nullable=False)
    products = relationship('Product', backref='user')

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.location = kwargs.get('location', None)
        self.password = generate_password_hash(kwargs.get('password'), method='sha256')
    
    def get_token(self):
        token = create_access_token(self.id)
        return token
    
    def save_to_db(self):
        session.add(self)
        session.commit()

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email', None)
        password = kwargs.get('password', None)
        user = cls.query.filter(cls.email == email).first()
        if not user or not check_password_hash(user.password, password):
             raise Exception('Not find user')
        return user

class Category(Base):
    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True)
    products = relationship('Product', backref='category')

    def save_to_db(self):
            session.add(self)
            session.commit()


class Product(Base):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=255), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    price = db.Column(db.String(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def save_to_db(self):
            session.add(self)
            session.commit()
