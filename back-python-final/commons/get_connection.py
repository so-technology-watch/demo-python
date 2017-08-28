# Python class for create database connection 
# Created on 2017-08-25 ( Time 18:18:33 )

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


class DataProvider(object):
    def __init__(self):
        """
        Connect to a database and provide data managing
        """
        # Database file
        url_database = 'sqlite:///sqlite_db.sqlite'
        engine_connect = create_engine(url_database, echo=True)

        self.session = sessionmaker(bind=engine_connect)()
        self.metadata = MetaData(engine_connect)


# To provide the same Base for all the entities
dp = DataProvider()
Base = declarative_base(metadata=dp.metadata)
