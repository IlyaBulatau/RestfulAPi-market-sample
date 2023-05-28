from flask.views import MethodView
from flask import request, jsonify, url_for, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.models import User, Product, Category
from market.serializers import ProductListSerializer, ProductDetailSerializer
from market.validators import ProductCreateValidater


class ProductListView(MethodView):
    decorators = [jwt_required()]

    def get(self):
        products = Product.query.all()
        serialier = ProductListSerializer(many=True)
        return jsonify(serialier.dump(products))
        
    
    def post(self):
        params = request.json
        user_id = get_jwt_identity()
    
        product = Product(**params)

        schema = ProductCreateValidater()
        serializaer = schema.dump(product)
        schema.load(serializaer)
        
        product.user_id = user_id

        product.save_to_db()

        user = product.user
        category = product.category

        serializaer = ProductDetailSerializer()
        serializaer.user = user
        serializaer.category = category
        result = serializaer.dump(product)

        return jsonify(result)

    
class ProductDetailView(MethodView):
    decorators = [jwt_required()]

    def get(self, product_id):
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            raise ValueError('This is product ID not found')

        schema = ProductDetailSerializer()

        user = product.user
        category = product.category

        schema.user_id = user
        schema.category = category

        serialier = schema.dump(product)

        return jsonify(serialier) 


    def put(self, product_id):
        params = request.json
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            raise Exception('This is product not found')
        if product.user.id != get_jwt_identity():
            raise Exception('This is not you product')
        product.change_data_to_db(**params)

        return redirect(url_for('.product_detail', product_id=product_id))


    def delete(self, product_id):
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            raise Exception('This is product not found')
        if product.user.id != get_jwt_identity():
            raise Exception('This is not you product')
        
        product.delete_from_db()
        return jsonify({
            "Message": f"Produtc with ID {product_id} delete"
        })
