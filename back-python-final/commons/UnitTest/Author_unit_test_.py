# Python class for unit test of Author 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Author import Author
from services import Author_service as commons_author_service
author_service = commons_author_service.AuthorService()

test_primary_key_1 = 200


class TestDaoAuthor(unittest.TestCase):

    def test_dao(self):

        print("--- test AuthorPersistence ")

        entity = Author()
        # --- Key values
        entity.id = test_primary_key_1
        # --- Other values
        entity.firstName = "test_value"
        entity.lastName = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        author_service.delete(entity)
        cpt_initial = author_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        author_service.insert(entity)
        self.assertTrue(author_service.exists_by_id(test_primary_key_1))
        self.assertTrue(author_service.exists(entity))

        cpt = author_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = author_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(author_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.firstName = "test_changement"
        entity.lastName = "test_changement"
        element = author_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = author_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = author_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(author_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(author_service.delete(entity), 0)

        cpt_final = author_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(author_service.exists_by_id(test_primary_key_1))
        self.assertFalse(author_service.exists(entity))
        self.assertEqual(author_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

