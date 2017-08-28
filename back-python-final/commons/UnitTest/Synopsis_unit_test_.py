# Python class for unit test of Synopsis 
# Created on 2017-08-25 ( Time 18:18:33 )

import unittest
import datetime

from entities.Synopsis import Synopsis
from services import Synopsis_service as commons_synopsis_service
synopsis_service = commons_synopsis_service.SynopsisService()

test_primary_key_1 = 200


class TestDaoSynopsis(unittest.TestCase):

    def test_dao(self):

        print("--- test SynopsisPersistence ")

        entity = Synopsis()
        # --- Key values
        entity.bookId = test_primary_key_1
        # --- Other values
        entity.synopsis = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        synopsis_service.delete(entity)
        cpt_initial = synopsis_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        synopsis_service.insert(entity)
        self.assertTrue(synopsis_service.exists_by_id(test_primary_key_1))
        self.assertTrue(synopsis_service.exists(entity))

        cpt = synopsis_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = synopsis_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(synopsis_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.synopsis = "test_changement"
        element = synopsis_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = synopsis_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = synopsis_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(synopsis_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(synopsis_service.delete(entity), 0)

        cpt_final = synopsis_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(synopsis_service.exists_by_id(test_primary_key_1))
        self.assertFalse(synopsis_service.exists(entity))
        self.assertEqual(synopsis_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

