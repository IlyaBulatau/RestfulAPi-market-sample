from flask.views import MethodView
from flask import request, jsonify

from database.models import User


class RegisterView(MethodView):

    def post(self):
        params = request.json
        user = User(**params)
        user.save_to_db()

        token = user.get_token()

        return jsonify({
            'You token': token
        })


class LoginView(MethodView):

    def post(self):
        params = request.json
        user = User.authenticate(**params)

        token = user.get_token()

        return jsonify({
            'token': token
        })
    