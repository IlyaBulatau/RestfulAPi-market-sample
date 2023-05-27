from environs import Env
from datetime import timedelta

class BaseConfig:
    env = Env()
    env.read_env()
    
    SECRET_KEY = env('SECRET_KEY')
    FLASK_APP = env('FLASK_APP')
    
class Costant:
    LEAVE_TIME_TOKEN = timedelta(hours=24)


class Development(BaseConfig):

    DEBUG = True
    FLASK_DEBUG = True

    JSON_SORT_KEYS = False
    
    JWT_ACCESS_TOKEN_EXPIRES = Costant.LEAVE_TIME_TOKEN


class DBConfig:
    env = Env()
    env.read_env()

    LOGIN = env('DB_LOGIN')
    PASSWORD = env('DB_PASSWORD')
    NAME = env('DB_NAME') 

    URL = f'postgresql+psycopg2://{LOGIN}:{PASSWORD}@localhost/{NAME}'   
