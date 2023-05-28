from flask.views import MethodView
from flask import request, jsonify
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
