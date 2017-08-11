import unittest
import datetime

from entities.Typesexe import Typesexe
from services import Typesexe_service as commons_typesexe_service
typesexe_service = commons_typesexe_service.TypesexeService("Typesexe")

test_primary_key_1 = 200


class TestDaoTypesexe(unittest.TestCase):

    def test_dao(self):

        # --- Init table
        init = Typesexe()
        init.idSexe = 100
        init.labelSexe = "test_value"

        print("--- test TypesexePersistence ")

        entity = Typesexe()
        # --- Key values
        entity.idSexe = test_primary_key_1
        # --- Other values
        entity.labelSexe = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        typesexe_service.delete_by_id(test_primary_key_1)
        cpt_initial = typesexe_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        element = typesexe_service.insert(entity)
        self.assertEqual(element, {"code": 201})
        self.assertTrue(typesexe_service.exists_by_id(test_primary_key_1))
        self.assertTrue(typesexe_service.exists(entity))

        cpt = typesexe_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = typesexe_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        self.assertTrue(typesexe_service.exists_by_id(test_primary_key_1))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.labelSexe = "test_changement"
        element = typesexe_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, {"entity": entity, "code": 200})

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = typesexe_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        print("Found : {}".format(element))

        # --- DELETE
        element = typesexe_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, {'entity': 1, 'code': 204})
        self.assertEqual(typesexe_service.delete_by_id(test_primary_key_1), {'entity': 0, 'code': 204})
        self.assertEqual(typesexe_service.delete(entity), {'entity': 0, 'code': 204})

        cpt_final = typesexe_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(typesexe_service.exists_by_id(test_primary_key_1))
        self.assertFalse(typesexe_service.exists(entity))
        self.assertEqual(typesexe_service.find_by_id(test_primary_key_1), {"entity": None, "code": 200})

        print("Normal end of persistence service test.")

