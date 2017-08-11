import unittest
import datetime

from entities.Eleve import Eleve
from services import Eleve_service as commons_eleve_service
eleve_service = commons_eleve_service.EleveService("Eleve")

test_primary_key_1 = 200


class TestDaoEleve(unittest.TestCase):

    def test_dao(self):

        # --- Init table
        init = Eleve()
        init.idEleve = 100
        init.nom = "test_value"
        init.prenom = "test_value"
        init.email = "test_value"
        init.password = "test_value"
        init.codePostal = "test_value"
        init.genre = 100		
        init.dateInscription = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

        print("--- test ElevePersistence ")

        entity = Eleve()
        # --- Key values
        entity.idEleve = test_primary_key_1
        # --- Other values
        entity.nom = "test_value"
        entity.prenom = "test_value"
        entity.email = "test_value"
        entity.password = "test_value"
        entity.codePostal = "test_value"
        entity.genre = 100		
        entity.dateInscription = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        eleve_service.delete_by_id(test_primary_key_1)
        cpt_initial = eleve_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        element = eleve_service.insert(entity)
        self.assertEqual(element, {"code": 201})
        self.assertTrue(eleve_service.exists_by_id(test_primary_key_1))
        self.assertTrue(eleve_service.exists(entity))

        cpt = eleve_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = eleve_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        self.assertTrue(eleve_service.exists_by_id(test_primary_key_1))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.nom = "test_changement"
        entity.prenom = "test_changement"
        entity.email = "test_changement"
        entity.password = "test_changement"
        entity.codePostal = "test_changement"
        entity.dateInscription = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        element = eleve_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, {"entity": entity, "code": 200})

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = eleve_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        print("Found : {}".format(element))

        # --- DELETE
        element = eleve_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, {'entity': 1, 'code': 204})
        self.assertEqual(eleve_service.delete_by_id(test_primary_key_1), {'entity': 0, 'code': 204})
        self.assertEqual(eleve_service.delete(entity), {'entity': 0, 'code': 204})

        cpt_final = eleve_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(eleve_service.exists_by_id(test_primary_key_1))
        self.assertFalse(eleve_service.exists(entity))
        self.assertEqual(eleve_service.find_by_id(test_primary_key_1), {"entity": None, "code": 200})

        print("Normal end of persistence service test.")

