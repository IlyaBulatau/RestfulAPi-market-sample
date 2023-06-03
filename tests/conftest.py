import pytest
import requests

import sys
sys.path.append('./src')

from database.models import User, Product, Category
from main import app as main_app


@pytest.yield_fixture()
def app():
    """
    Create app
    """
    _app = main_app
    
    yield _app


@pytest.yield_fixture()
def client(app):
    """
    Create test client
    """
    with app.test_client() as client:

        yield client

@pytest.fixture()
def product_params():
    """
    Create params for request add product
    """
    product = { 'name': 'T-shert', 
                'description': 'Very cool cloth', 
                'price': '130', 
                'category_id': 1,}
    return product

@pytest.fixture()
def dns():
    return 'http://127.0.0.1:5000'

@pytest.fixture()
def token(dns):
    """
    Process auth and get token
    """
    params = {'email': 'artem@mail.ru', 'password': '1234'}
    get_token = requests.post(dns+'/api/auth/login', json=params).json()
    token = get_token.get('token')
    return token

@pytest.fixture()
def headers(token):
    """
    Create headers for requests
    """
    headers = {"Authorization": f"Bearer {token}"}
    return headers

@pytest.fixture()
def product_id(product_params):
    """
    Get product ID in database
    """
    product = Product.query.filter(Product.name == product_params['name']).first()
    return product.id



