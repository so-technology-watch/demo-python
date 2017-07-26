from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from commons.get_connexion import DataProvider as dataProvider
from sqlalchemy import *
from sqlalchemy.orm import *

from sqlalchemy.engine import Engine
from sqlalchemy import event

invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class GenericDao(object):
    def __init__(self, table_name, entity_type):
        self.table_name = table_name
        self.entity_type = entity_type
        self.dataProvider = dataProvider()
        self.table = Table(table_name, self.dataProvider.metadata, autoload=True)
        self.table_mapper = mapper(entity_type, self.table)

    def get_connexion(self):
        return self.dataProvider.session

    def close_connexion(self, _session):
        if _session is not None:
            try:
                _session.close()
            except SQLAlchemyError as e:
                raise e

    def do_select_all(self):
        try:
            session = self.get_connexion()
        except SQLAlchemyError as e:
            test = list(e.__dict__.values())
            return test[2]
        return session.query(self.entity_type).all()

    def do_select(self, query):
        try:
            session = self.get_connexion()
            entity = session.query(self.entity_type).filter(query).first()
        except SQLAlchemyError as e:
            test = list(e.__dict__.values())
            return test[2]
        return entity

    def do_select_multiple_keys(self, query, query2):
        try:
            session = self.get_connexion()
            entity = session.query(self.entity_type).filter(and_(query, query2)).first()
        except SQLAlchemyError as e:
            test = list(e.__dict__.values())
            return test[2]
        return entity

    def do_insert(self, entity):
        session = None
        try:
            session = self.get_connexion()
            session.add(entity)
            session.commit()
            return 200
        except SQLAlchemyError as e:
            session.rollback()
            test = list(e.__dict__.values())
            return test[2]

    def do_update(self, entity, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).update(entity.to_dict())
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            test = list(e.__dict__.values())
            return test[2]
        return result

    def do_update_multiple_keys(self, entity, _query, _query2):
        _session = None
        try:
            _session = self.get_connexion()
            result = _session.query(self.entity_type).filter(and_(_query, _query2)).update(entity.to_dict())
            _session.commit()
        except SQLAlchemyError as e:
            _session.rollback()
            test = list(e.__dict__.values())
            return test[2]
        return result

    def do_exist(self, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).exists()
        except SQLAlchemyError as e:
            test = list(e.__dict__.values())
            return test[2]
        return result

    def do_count_all(self):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).count()
        except SQLAlchemyError as e:
            session.rollback()
            test = list(e.__dict__.values())
            return test[2]
        return result

    def do_delete(self, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).delete()
            session.commit()
        except SQLAlchemyError as e:
            test = list(e.__dict__.values())
            return test[2]
        return result

    def do_delete_multiple_key(self, _query, _query2):
        try:
            _session = self.get_connexion()
            result = _session.query(self.entity_type).filter(and_(_query, _query2)).delete()
            _session.commit()
        except SQLAlchemyError as e:
            test = list(e.__dict__.values())
            return test[2]
        return result