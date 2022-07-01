from os import environ, path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://' + environ["POSTGRES_USERNAME"] + ':' + environ["POSTGRES_PASSWORD"] + '@' + environ["POSTGRES_HOST"] + '/' + environ["POSTGRES_DATABASE"]

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()