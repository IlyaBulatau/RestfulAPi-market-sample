from flask import Blueprint

from authentication import views

auth = Blueprint('auth', __name__)

auth.add_url_rule('/register', view_func=views.RegisterView.as_view('register'))
auth.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
