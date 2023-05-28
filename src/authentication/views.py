from flask.views import MethodView
from flask import request, jsonify

from database.models import User
from authentication.validators import RegisterShemaValidator
from log.log import log

class RegisterView(MethodView):

    def post(self):
        params = request.json
        user = User(**params)
        
        try:
            shema = RegisterShemaValidator()
            serialize = shema.dump(user)
            shema.load(serialize)
        except Exception as e:
            log.warning(str(e))
            return jsonify({
                'Message Error': str(e) 
            })

        try:
            user.save_to_db()
            log.info(f'Register New User ID: {user.id}')
        except Exception as e:
            return jsonify({
                'Message Error': str(e)
            })

        token = user.get_token()
        log.info(f'User: ID {user.id} get token: {token}')

        return jsonify({
            'You token': token
        })


class LoginView(MethodView):

    def post(self):
        params = request.json
        try:
            user = User.authenticate(**params)
        except Exception as e:
            log.warning(str(e))
            return jsonify({
                'Message Error': str(e)
            })

        token = user.get_token()
        log.info(f'User: ID {user.id} get token: {token}')
        
        return jsonify({
            'token': token
        })
    