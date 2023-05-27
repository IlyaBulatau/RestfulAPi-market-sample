from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from config import DBConfig

engine = create_engine(DBConfig.URL)
session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
Base = declarative_base()
Base.query = session.query_property()