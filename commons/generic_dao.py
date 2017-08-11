from sqlalchemy.exc import SQLAlchemyError
from commons.get_connexion import DataProvider as dataProvider
from sqlalchemy import *
from sqlalchemy.engine import Engine
from sqlalchemy import event


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

    def get_connexion(self):
        return self.dataProvider.session

    def do_select_all(self):
        try:
            session = self.get_connexion()
            return session.query(self.entity_type).all()
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_select(self, query):
        try:
            session = self.get_connexion()
            entity = session.query(self.entity_type).filter(query).first()
            return {"entity": entity, "code": 200}
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_insert(self, entity, query):
        session = None
        try:
            session = self.get_connexion()
            exist = self.do_select(query)
            if exist['entity']:
                return {"code": 409} 
            else:
                session.add(entity)
                session.commit()
                return {"code": 201}
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            return {"code": 500, "message": e} 

    def do_update(self, entity, query):
        session = None
        try:
            session = self.get_connexion()
            exist = self.do_select(query)
            if exist['entity']:
                session.query(self.entity_type).filter(query).update(entity.to_dict(), synchronize_session='fetch')
                session.commit()
                return {"entity": entity, "code": 200}
            else:
                session.add(entity)
                session.commit()
                return {"entity": entity, "code": 201}
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            return {"code": 500, "message": e} 

    def do_delete(self, query):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).filter(query).delete(synchronize_session='fetch')
            session.commit()
            return {"entity": result, "code": 204}
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_count_all(self):
        try:
            session = self.get_connexion()
            result = session.query(self.entity_type).count()
            return result
        except SQLAlchemyError as e:
            print(e)
            return e

    def do_exists(self, query):
        try:
            session = self.get_connexion()
            q = session.query(self.entity_type).filter(query)
            return session.query(q.exists()).scalar()
        except SQLAlchemyError as e:
            print(e)
            return e

