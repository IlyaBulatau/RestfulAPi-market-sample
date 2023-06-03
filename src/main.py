from flask import Flask
from flask_jwt_extended import JWTManager
import flask

from database.connect import Base, session, engine

from market.market import market
from authentication.auth import auth
from errors.handlers import register_all_errors_from_app
import config
from log.log import log
from flask_swagger_ui import get_swaggerui_blueprint


flask.json.provider.DefaultJSONProvider.sort_keys = False

app = Flask(__name__)
app.config.from_object(config.Development)
app.logger.addHandler(log)


swagget = get_swaggerui_blueprint(base_url='/api/docs', api_url='/static/swagger.yaml')
app.register_blueprint(swagget)


jwt = JWTManager()
jwt.init_app(app)

register_all_errors_from_app(app)

app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(market, url_prefix='/api/market')

app.teardown_appcontext
def close_session(exception=None):
    session.remove()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run()

