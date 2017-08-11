import unittest
import datetime

from entities.Cours import Cours
from services import Cours_service as commons_cours_service
cours_service = commons_cours_service.CoursService("Cours")

test_primary_key_1 = 200


class TestDaoCours(unittest.TestCase):

    def test_dao(self):

        # --- Init table
        init = Cours()
        init.idCours = 100
        init.libelle = "test_value"
        init.nbHeures = 1

        print("--- test CoursPersistence ")

        entity = Cours()
        # --- Key values
        entity.idCours = test_primary_key_1
        # --- Other values
        entity.libelle = "test_value"
        entity.nbHeures = 1

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        cours_service.delete_by_id(test_primary_key_1)
        cpt_initial = cours_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        element = cours_service.insert(entity)
        self.assertEqual(element, {"code": 201})
        self.assertTrue(cours_service.exists_by_id(test_primary_key_1))
        self.assertTrue(cours_service.exists(entity))

        cpt = cours_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = cours_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        self.assertTrue(cours_service.exists_by_id(test_primary_key_1))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.libelle = "test_changement"
        entity.nbHeures = 2
        element = cours_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, {"entity": entity, "code": 200})

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = cours_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        print("Found : {}".format(element))

        # --- DELETE
        element = cours_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, {'entity': 1, 'code': 204})
        self.assertEqual(cours_service.delete_by_id(test_primary_key_1), {'entity': 0, 'code': 204})
        self.assertEqual(cours_service.delete(entity), {'entity': 0, 'code': 204})

        cpt_final = cours_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(cours_service.exists_by_id(test_primary_key_1))
        self.assertFalse(cours_service.exists(entity))
        self.assertEqual(cours_service.find_by_id(test_primary_key_1), {"entity": None, "code": 200})

        print("Normal end of persistence service test.")

