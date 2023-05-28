from flask.views import MethodView
from flask import request, jsonify, url_for, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.models import User, Product, Category
from market.serializers import ProductListSerializer, ProductDetailSerializer
from market.validators import ProductCreateValidater
from log.log import log


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

        try:
            schema = ProductCreateValidater()
            serializaer = schema.dump(product)
            schema.load(serializaer)
        except Exception as e:
            msg = e.args[0].get('_schema')
            log.warning(msg)
            return jsonify({
                'Message Error': msg
            })

        product.user_id = user_id

        try:
            product.save_to_db()
        except Exception as e:
            log.warning(str(e))
            return jsonify({
                'Message Error': str(e)
            })

        user = product.user
        category = product.category

        serializaer = ProductDetailSerializer()
        serializaer.user = user
        serializaer.category = category
        result = serializaer.dump(product)

        log.info(f'UserID: {user_id} add new product with ID: {product.id}')
        return jsonify(result)

    
class ProductDetailView(MethodView):
    decorators = [jwt_required()]

    def get(self, product_id):
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            log.warning('This is product ID not found')
            return jsonify({
                'Message Error': 'This is product ID not found'
            })

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
            log.warning('This is product not found')
            return jsonify({
                "Message Error": "This is product not found"
            })
        if product.user.id != get_jwt_identity():
            log.warning('This is not you product')
            return jsonify({
                'Message Error': 'This is not you product' 
            })
            
        try:
            product.change_data_to_db(**params)
            log.info(f'UserID: {product.user.id} change porduct with ID: {product.id}')
        except Exception as e:
            log.warning(str(e))
            return jsonify({
                'Message Error': str(e)
            })

        return redirect(url_for('.product_detail', product_id=product_id))


    def delete(self, product_id):
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            log.warning('This is product not found')
            return jsonify({
                'Message Error': 'This is product not found' 
            })
    
        if product.user.id != get_jwt_identity():
            log.warning('This is not you product')
            return jsonify({
                'Message Error': 'This is not you product'
            })

        try:
            log.info(f'UserID: {product.user.id} delete product with ID: {product.id}')        
            product.delete_from_db()
        except Exception as e:
            return jsonify({
                'Message Error': str(e)
            })

        return jsonify({
            "Message": f"Produtc with ID {product_id} delete"
        })
