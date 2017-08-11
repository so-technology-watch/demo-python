import unittest
import datetime

from entities.Typemention import Typemention
from services import Typemention_service as commons_typemention_service
typemention_service = commons_typemention_service.TypementionService("Typemention")

test_primary_key_1 = 200


class TestDaoTypemention(unittest.TestCase):

    def test_dao(self):

        # --- Init table
        init = Typemention()
        init.idMention = 100
        init.labelMention = "test_value"

        print("--- test TypementionPersistence ")

        entity = Typemention()
        # --- Key values
        entity.idMention = test_primary_key_1
        # --- Other values
        entity.labelMention = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        typemention_service.delete_by_id(test_primary_key_1)
        cpt_initial = typemention_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        element = typemention_service.insert(entity)
        self.assertEqual(element, {"code": 201})
        self.assertTrue(typemention_service.exists_by_id(test_primary_key_1))
        self.assertTrue(typemention_service.exists(entity))

        cpt = typemention_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = typemention_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        self.assertTrue(typemention_service.exists_by_id(test_primary_key_1))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.labelMention = "test_changement"
        element = typemention_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, {"entity": entity, "code": 200})

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = typemention_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        print("Found : {}".format(element))

        # --- DELETE
        element = typemention_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, {'entity': 1, 'code': 204})
        self.assertEqual(typemention_service.delete_by_id(test_primary_key_1), {'entity': 0, 'code': 204})
        self.assertEqual(typemention_service.delete(entity), {'entity': 0, 'code': 204})

        cpt_final = typemention_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(typemention_service.exists_by_id(test_primary_key_1))
        self.assertFalse(typemention_service.exists(entity))
        self.assertEqual(typemention_service.find_by_id(test_primary_key_1), {"entity": None, "code": 200})

        print("Normal end of persistence service test.")

