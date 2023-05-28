from flask import Flask
from flask_jwt_extended import JWTManager

from database.connect import Base, session, engine
from database.models import User, Category, Product

from market.market import market
from authentication.auth import auth
import config
from log.log import log


app = Flask(__name__)
app.config.from_object('config.Development')
app.logger.addHandler(log)

jwt = JWTManager()
jwt.init_app(app)


app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(market, url_prefix='/api/market')

app.teardown_appcontext
def close_session(exception=None):
    session.remove()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run()

# TODO - обработка исключений и ошибок 