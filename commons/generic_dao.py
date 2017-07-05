from sqlalchemy.exc import SQLAlchemyError
from commons.get_connexion import DataProvider as dataProvider
from sqlalchemy import *
from sqlalchemy.orm import *


class GenericDao(object):
    def __init__(self, table_name, entity_type):
        self.table_name = table_name
        self.entity_type = entity_type
        self.dataProvider = dataProvider()
        self.table = Table(table_name, self.dataProvider.metadata, autoload=True)
        self.table_mapper = mapper(entity_type, self.table)

    def get_connexion(self):
        return self.dataProvider.session

    def close_connexion(self, session):
        if session is not None:
            try:
                session.close()
            except SQLAlchemyError as e:
                raise (e)

    def do_select_all(self):
        try:
            session = self.get_connexion()
        except SQLAlchemyError as e:
            raise (e)
        return session.query(self.entity_type).all()

    def do_select(self, query):
        try:
            session = self.get_connexion()
            entity = session.query(self.entity_type).filter(query).first()
        except SQLAlchemyError as e:
            raise (e)
        return entity

    def do_insert(self, entity):
        session = None
        try:
            session = self.get_connexion()
            session.add(entity)
            session.commit()
            return entity
        except SQLAlchemyError as e:
            session.rollback()
            raise (e)

    def do_update(self, entity, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).update(entity.to_dict())
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise (e)
        return result

    def do_exist(self, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).exists()
        except SQLAlchemyError as e:
            raise (e)
        return result

    def do_count_all(self):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).count()
        except SQLAlchemyError as e:
            session.rollback()
            raise (e)
        return result

    def do_delete(self, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).delete()
            session.commit()
        except SQLAlchemyError as e:
            raise (e)
        return result