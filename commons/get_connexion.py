from configparser import ConfigParser
from sqlalchemy import *
from sqlalchemy.orm import *


class DataProvider(object):
    def __init__(self):
        engine = create_connexion()
        self.session = sessionmaker(bind=engine)()
        self.metadata = MetaData(engine)


def create_connexion():
    config = ConfigParser()
    config.read('C:/Users/aurlucas/PycharmProjects/bottle-sqlalchemy/commons/config.cfg')
    database_url = config.get('database', 'url_database')
    engine = create_engine(database_url, echo=True)
    return engine

