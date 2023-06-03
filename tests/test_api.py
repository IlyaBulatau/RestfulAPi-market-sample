import pytest


def test_get_token(token):
    assert token != None


class TestProductApi:

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

    def test_get_product_by_id(self, client, product_id, headers):
        """
        GET '/api/market/products/id'
        """
        req = client.get(f'/api/market/products/{product_id}', headers=headers)
        assert req.status_code == 200
        assert 'Message Error' not in req.json

    def test_change_product(self, client, headers, product_id, product_params):
        """
        PUT /api/market/products/id/change
        """
        req = client.put(f'/api/market/products/{product_id}/change', headers=headers, json=product_params)
        assert req.status_code == 302

    def test_delete_product(self, client, headers, product_id):
        """
        DELETE /api/market/products/id/delete
        """
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




