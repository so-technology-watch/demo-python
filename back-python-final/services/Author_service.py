# Python class for service of Author 
# Created on 2017-08-25 ( Time 18:18:32 )

import commons.generic_dao as dao_commons
from entities.Author import Author
from sqlalchemy import text
from services.commons import common_service


class AuthorService:
    def __init__(self):
        self.dao = dao_commons.GenericDao(Author)

    def find_by_id(self, id):
        """
        Tries to find an entity using its Id / Primary Key
        :param id: PK of the entity to find
        :return: False if entity not found, entity if found
        """
        request = build_query(id)
        return common_service.find_by_id(self.dao, request)

    def find_all(self):
        """
        Finds all entities.
        :return:  all entities
        """
        return common_service.find_all(self.dao)

    def insert(self, entity):
        """
        Insert the given entity in the database
        :param entity: to be inserted (supposed to have a valid Id/PK )
        :return: false if not found, entity if found
        """
        request = build_query(entity.id)
        return common_service.insert(self.dao, request, entity)

    def update(self, entity):
        """
        Updates the given entity in the database
        :param entity: to be updated (supposed to have a valid Id/PK )
        :return: true if entity updated, false if not found
        """
        request = build_query(entity.id)
        return common_service.update(self.dao, request, entity)

    def save(self, entity):
        """
        Updates or creates the given entity in the database
        :param entity: to be updated or created (supposed to have a valid Id/PK )
        :return: json with isNew attribute (True if created) and entity (created or updated)
        """
        request = build_query(entity.id)
        return common_service.save(self.dao, request, entity)

    def delete_by_id(self, id):
        """
        Deletes an entity using its Id / Primary Key
        :param id: PK of the entity to delete
        :return: true if the entity has been deleted, false if not found and not deleted
        """
        request = build_query(id)
        return common_service.delete_by_id(self.dao, request)

    def delete(self, entity):
        """
        Deletes an entity
        :param entity: to delete
        :return: 1 if the entity has been deleted, 0 if not found and not deleted
        """
        request = build_query(entity.id)
        return common_service.delete(self.dao, request)

    def exists_by_id(self, id):
        """
        Ckeck if an Id / Primary Key is in the entity table
        :param id: PK to check in database
        :return: true or false
        """
        request = build_query(id)
        return common_service.exists_by_id(self.dao, request)

    def exists(self, entity):
        """
        Ckeck if an entity is in the entity table
        :return: true or false
        """
        request = build_query(entity.id)
        return common_service.exists(self.dao, request)

    def count_all(self):
        """
        Counts all the entity present in the entity table
        :return: the number of rows in the entity table
        """
        return common_service.count_all(self.dao)


def build_query(id):
    return text("Author.id == '{}'".format(id))
