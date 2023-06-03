import pytest
import requests
import sys
sys.path.append('./src')

@pytest.fixture()
def token():
    params = {'email': 'artem@mail.ru', 'password': '1234'}
    get_token = requests.post('http://127.0.0.1:5000/api/auth/login', json=params).json()
    token = get_token.get('token')
    return token

# TOKEN = requet_to_get_token()
@pytest.fixture()
def headers(token):
    headers = {"Authorization": f"Bearer {token}"}
    return headers

DATA = {
    "name": "Notebook TECHNO",
    "price": "11000",
    "category_id": "3"
}   

def test_get_products_list(headers):
    """
    GET /api/market/products
    """
    req = requests.get('http://127.0.0.1:5000/api/market/products', headers=headers)
    assert req.status_code == 200

def test_get_my_products_list(headers):
    """
    GET /api/market/products/my_products
    """
    req = requests.get('http://127.0.0.1:5000/api/market/products/my_products', headers=headers)
    assert req.status_code == 200

def test_get_categories_list(headers):
    """
    GET /api/market/categories
    """
    req = requests.get('http://127.0.0.1:5000/api/market/categories', headers=headers)
    assert req.status_code == 200

def test_get_categories_by_id(headers):
    """
    GET /api/market/products/my_products/1
    """
    req = requests.get('http://127.0.0.1:5000/api/market/categories/1', headers=headers)
    assert req.status_code == 200

def test_get_products_by_id(headers):
    """
    GET /api/market/products/my_products
    """
    req = requests.get('http://127.0.0.1:5000/api/market/products/1', headers=headers)
    assert req.status_code == 200

# def test_add_new_product():
#     """
#     POST /api/market/products
#     """
#     req = requests.post('http://127.0.0.1:5000/api/market/products', json=DATA, headers=headers)
#     assert 'Message Error' not in req.json()
#     assert req.status_code == 200

# def test_delete_product_by_id():
#     """
#     """
