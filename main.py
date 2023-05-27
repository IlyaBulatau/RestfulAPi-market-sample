from flask import Flask

from database.connect import Base, session, engine
from database.models import User, Category, Product

app = Flask(__name__)

app.config.from_object()

app.teardown_appcontext
def close_session(exception=None):
    session.remove()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run()