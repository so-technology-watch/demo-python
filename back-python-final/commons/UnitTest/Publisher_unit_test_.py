# Python class for unit test of Publisher 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Publisher import Publisher
from services import Publisher_service as commons_publisher_service
publisher_service = commons_publisher_service.PublisherService()

test_primary_key_1 = 200


class TestDaoPublisher(unittest.TestCase):

    def test_dao(self):

        print("--- test PublisherPersistence ")

        entity = Publisher()
        # --- Key values
        entity.code = test_primary_key_1
        # --- Other values
        entity.countryCode = "AAA"
        entity.name = "test_value"
        entity.email = "test_value"
        entity.contact = "test_value"
        entity.city = "test_value"
        entity.zipCode = 1
        entity.phone = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        publisher_service.delete(entity)
        cpt_initial = publisher_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        publisher_service.insert(entity)
        self.assertTrue(publisher_service.exists_by_id(test_primary_key_1))
        self.assertTrue(publisher_service.exists(entity))

        cpt = publisher_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = publisher_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(publisher_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.name = "test_changement"
        entity.email = "test_changement"
        entity.contact = "test_changement"
        entity.city = "test_changement"
        entity.zipCode = 2
        entity.phone = "test_changement"
        element = publisher_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = publisher_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = publisher_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(publisher_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(publisher_service.delete(entity), 0)

        cpt_final = publisher_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(publisher_service.exists_by_id(test_primary_key_1))
        self.assertFalse(publisher_service.exists(entity))
        self.assertEqual(publisher_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

