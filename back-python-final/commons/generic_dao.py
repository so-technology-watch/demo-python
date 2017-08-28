# Python class for Generic Dao
# Created on 2017-08-25 ( Time 18:18:33 )

from sqlalchemy.exc import SQLAlchemyError
from commons.get_connection import DataProvider as dataProvider
from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_pragma(db_connection, connection_record):
    """
    In case of SQLite database, allow foreign keys
    :param db_connection:
    :return: foreign keys turned on 
    """
    cursor = db_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class GenericDao(object):
    def __init__(self, table_name):
        # Name of the table in database for requests
        self.table_name = table_name
        # Data provider to manage the data of the database
        self.dataProvider = dataProvider()

    def get_connection(self):
        """
        Open connection with the database
        """
        return self.dataProvider.session

    def do_select_all(self):
        """
        Select all entities from the database
        :param: 
        :return: all the entities's objects if found, an error message if problems with the database
        """
        try:
            session = self.get_connection()
            return session.query(self.table_name).all()
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_select(self, query):
        """
        Select an entity by her primary key in the database
        :param query: conditions of the request (the PK)
        :return: the entity if found, an error message if problems with the database
        """
        try:
            session = self.get_connection()
            entity = session.query(self.table_name).filter(query).first()
            return entity
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_insert(self, entity):
        """
        Create the given entity in the database
        :param entity: to be created (supposed to have a valid Id/PK )
        :return: entity if created, an error message if problems with the database
        """
        session = None
        try:
            session = self.get_connection()
            session.add(entity)
            session.commit()
            return entity
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            return e

    def do_update(self, entity, query):
        """
        Update the given entity in the database 
        :param entity: to be updated (supposed to have a valid Id/PK )
        :param query: conditions of the request (the PK)
        :return: 1 if the entity has been updated, 0 if not, an error message if problems with the database
        """
        session = None
        try:
            session = self.get_connection()
            result = session.query(self.table_name).filter(query).update(entity.to_dict(), synchronize_session='fetch')
            session.commit()
            return result
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            return e

    def do_delete(self, query):
        """
        Delete an entity in the database
        :param query: conditions of the request (the PK)
        :return: 1 if the entity has been deleted, 0 if not, an error message if problems with the database
        """
        session = None
        try:
            session = self.get_connection()
            result = session.query(self.table_name).filter(query).delete(synchronize_session='fetch')
            session.commit()
            return result
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            return e

    def do_count_all(self):
        """
        Count all entities in the database
        :param:
        :return: number of entities (integer), an error message if problems with the database
        """
        try:
            session = self.get_connection()
            result = session.query(self.table_name).count()
            return result
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_exists(self, query):
        """
        Check if an entity exists in the database
        :param query: conditions of the request (the PK)
        :return: true if the entity exists, false if not, an error message if problems with the database
        """
        try:
            session = self.get_connection()
            q = session.query(self.table_name).filter(query)
            return session.query(q.exists()).scalar()
        except SQLAlchemyError as e:
            print(e)
            return e
