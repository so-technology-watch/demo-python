from configparser import ConfigParser
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataProvider(object):
    def __init__(self):
        engine_connect = create_connexion()
        self.session = sessionmaker(bind=engine_connect)()
        self.metadata = MetaData(engine_connect)


def create_connexion():
    config = ConfigParser()
    config.read('C:/Users/aurlucas/PycharmProjects/back-python/commons/config.cfg')
    database_url = config.get('database', 'url_database')
    engine = create_engine(database_url, echo=True)
    # Base.metadata.create_all(engine)
    return engine
