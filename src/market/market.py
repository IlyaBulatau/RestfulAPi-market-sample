from flask import Blueprint

from market import views

market = Blueprint('market', __name__)

market.add_url_rule('/products', view_func=views.ProductListView.as_view('products'), methods=['GET', 'POST'])
market.add_url_rule('/products/my_products', view_func=views.MyProductView.as_view('my_products'), methods=['GET'])
market.add_url_rule('/categories', view_func=views.CategoryListView.as_view('categories'), methods=['GET'])
market.add_url_rule('/categories/<int:category_id>', view_func=views.ProductByCategoryView.as_view('product_by_categories'), methods=['GET'])
market.add_url_rule('/products/<int:product_id>', view_func=views.ProductDetailView.as_view('product_detail'), methods=['POST', 'GET'])
market.add_url_rule('/products/<int:product_id>/delete', view_func=views.ProductDetailView.as_view('product_delete'), methods=['DELETE'])
market.add_url_rule('/products/<int:product_id>/change', view_func=views.ProductDetailView.as_view('product_change'), methods=['PUT'])