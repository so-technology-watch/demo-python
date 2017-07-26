import commons.generic_dao as dao_commons
from entities.Car import Car


class CarService:
    def __init__(self, entity):
        self.dao = dao_commons.GenericDao(entity, Car)

    def find_by_id(self, _id):
        """
        Tries to find an entity using its Id / Primary Key
        :param _id:
        :return: entity
        """
        entity = new_instance_with_primary_key(_id)
        query = build_query(entity)
        return self.dao.do_select(query)

    def find_all(self):
        """
        Finds all entities.
        :return:  all entities
        """
        return self.dao.do_select_all()

    def find(self, entity):
        """
        Tries to find the given entity
        :param entity:
        :param self:
        :return: entity
        """
        query = build_query(entity)
        return self.dao.do_select(query)

    def insert(self, entity):
        """
        Insert the given entity in the database
        :param entity: to be inserted (supposed to have a valid Id/PK )
        :return: entity
        """
        return self.dao.do_insert(entity)

    def update(self, entity):
        """
        Updates the given entity in the database
        :param entity: to be updated (supposed to have a valid Id/PK )
        :return: true if the entity has been updated, false if not found and not updated
        """
        query = build_query(entity)
        result = self.dao.do_update(entity, query)
        return result > 0

    def save(self, entity):
        """
        Saves the given entity in the database (create or update)
        :param entity: to be saved (supposed to have a valid Id/PK )
        :return: entity
        """
        if exists(entity):
            return self.update(entity)
        else:
            return self.insert(entity)

    def delete_by_id(self, _id):
        """
        Deletes an entity using its Id / Primary Key
        :param _id:
        :return: true if the entity has been deleted, false if not found and not deleted
        """
        entity = new_instance_with_primary_key(_id)
        query = build_query(entity)
        result = self.dao.do_delete(query)
        return result > 0


def delete(entity):
    """
    Deletes an entity using the Id / Primary Key stored in the given object
    :param entity: to be deleted (supposed to have a valid Id/PK )
    :return: true if the entity has been deleted, false if not found and not deleted
    """
    query = build_query(entity)
    result = dao_commons.do_delete(query)
    return result > 0


def exists_by_id(_id):
    """
    check if an entity exists with the given Id / Primary Key
    :param _id:
    :return: true if an entity exists with the given Id / Primary Key
    """
    entity = new_instance_with_primary_key(_id)
    query = build_query(entity)
    return dao_commons.do_exists(query)


def exists(entity):
    """
    check if the given entity exist
    :param entity:
    :return: true if the given entity exist
    """
    query = build_query(entity)
    return dao_commons.do_exists(query)


def count_all():
    """
    Counts all the entity present in the entity table
    :return: the number of rows in the entity table
    """
    return dao_commons.do_count_all()


def new_instance_with_primary_key(_id):
    """
    build new entity with the given _id
    :param _id:
    :return: entity with the given _id
    """
    entity = Car(_id, None, None, None, None)
    return entity


def build_query(entity):
    return Car.id == '%s' % entity.id
