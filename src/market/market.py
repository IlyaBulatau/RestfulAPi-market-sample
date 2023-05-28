from flask import Blueprint

from market import views

market = Blueprint('market', __name__)

market.add_url_rule('/products', view_func=views.ProductListView.as_view('products'), methods=['GET', 'POST'])
market.add_url_rule('/products/<int:product_id>', view_func=views.ProductDetailView.as_view('product_detail'), methods=['POST', 'GET'])
market.add_url_rule('/products/<int:product_id>/delete', view_func=views.ProductDetailView.as_view('product_delete'), methods=['DELETE'])
market.add_url_rule('/products/<int:product_id>/change', view_func=views.ProductDetailView.as_view('product_change'), methods=['PUT'])