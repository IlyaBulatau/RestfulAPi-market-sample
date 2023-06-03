import sys
sys.path.append('./src')

from database.models import Product


def test_register_process(client, auth_params):
    """
    POST /api/aut/register
    """
    req = client.post('api/auth/register', json=auth_params)
    assert req.status_code == 200

def test_get_token(token):
    assert token != None


class TestProductApi:

    def get_product_id(self, product_name):
        """
        Get product ID in database
        """
        product = Product.query.filter(Product.name == product_name).first()
        return product.id


    def test_get_products_list(self, client, headers):
        """
        GET /api/market/products
        """
        req = client.get('/api/market/products', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json

    def test_get_my_product_list(self, client, headers):
        """
        GET /api/market/products/my_products
        """
        req = client.get('/api/market/products/my_products', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json

    def test_add_new_product(self, client, headers, product_params):
        """
        POST /api/market/products
        """
        req = client.post('/api/market/products', headers=headers, json=product_params)
        assert req.status_code == 200
        assert 'Message Error' not in req.json

    def test_get_product_by_id(self, client, product_params, headers):
        """
        GET '/api/market/products/id'
        """
        product_id = self.get_product_id(product_params['name'])
        req = client.get(f'/api/market/products/{product_id}', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json

    def test_change_product(self, client, headers, product_params):
        """
        PUT /api/market/products/id/change
        """
        product_id = self.get_product_id(product_params['name'])
        req = client.put(f'/api/market/products/{product_id}/change', headers=headers, json=product_params)
        assert req.status_code == 302

    def test_delete_product(self, client, headers, product_params):
        """
        DELETE /api/market/products/id/delete
        """
        product_id = self.get_product_id(product_params['name'])
        req = client.delete(f'/api/market/products/{product_id}/delete', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json




class TestCategoryApi:

    def test_get_categories_list(self, client, headers):
        """
        GET /api/market/categories
        """
        req = client.get('/api/market/categories', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json

    def test_get_categories_by_id(self, client, headers):
        """
        GET /api/market/products/my_products/1
        """
        req = client.get('/api/market/categories/1', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json




