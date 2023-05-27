from flask import Flask

from database.connect import Base, session, engine
from database.models import User, Category, Product
from authentication.auth import auth
import config

from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(config.Development)

jwt = JWTManager()
jwt.init_app(app)


app.register_blueprint(auth, url_prefix='/api/auth')

app.teardown_appcontext
def close_session(exception=None):
    session.remove()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run()

# TODO - сделать сериализатор для возврата данных
# сделать валидацию данных до отправки в БД
# сделать CRUD запросы для товаров
# настроить логирование
# обработка исключений и ошибок 