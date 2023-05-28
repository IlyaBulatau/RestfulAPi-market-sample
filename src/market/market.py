from flask import Blueprint

from market import views

market = Blueprint('market', __name__)

market.add_url_rule('/products', view_func=views.ProductListView.as_view('products'))
market.add_url_rule('/products/<int:product_id>', view_func=views.ProductDetailView.as_view('product_detail'))