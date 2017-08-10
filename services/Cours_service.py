import commons.generic_dao as dao_commons
from entities.Cours import Cours


class CoursService:
    def __init__(self, entity):
        self.dao = dao_commons.GenericDao(entity, Cours)

    def find_by_id(self, idCours):
        """
        Tries to find an entity using its Id / Primary Key
        :param _id:
        :return: entity
        """
        request = build_query(idCours)
        query = sqlalchemy_query(request)
        return self.dao.do_select(query)

    def find_all(self):
        """
        Finds all entities.
        :return:  all entities
        """
        return self.dao.do_select_all()

    def insert(self, entity):
        """
        Insert the given entity in the database
        :param entity: to be inserted (supposed to have a valid Id/PK )
        :return: entity
        """
        request = build_query(entity.idCours)
        query = sqlalchemy_query(request)
        return self.dao.do_insert(entity, query)

    def update(self, entity):
        """
        Updates the given entity in the database
        :param entity: to be updated (supposed to have a valid Id/PK )
        :return: true if the entity has been updated, false if not found and not updated
        """
        request = build_query(entity.idCours)
        query = sqlalchemy_query(request)
        return self.dao.do_update(entity, query)

    def delete_by_id(self, idCours):
        """
        Deletes an entity using its Id / Primary Key
        :param _id:
        :return: true if the entity has been deleted, false if not found and not deleted
        """
        request = build_query(idCours)
        query = sqlalchemy_query(request)
        return self.dao.do_delete(query)

    def count_all(self):
        """
        Counts all the entity present in the entity table
        :return: the number of rows in the entity table
        """
        return self.dao.do_count_all()


def build_query(idCours):
    return {
        "id_1": 'Cours.idCours == {}'.format(idCours),
    }


def sqlalchemy_query(request):
        cpt = 0
        query = ""
        for value in request:
            cpt = cpt + 1
            if cpt < len(request):
                query = query + request[value] + " and "
            else:
                query = query + request[value]
        return query
