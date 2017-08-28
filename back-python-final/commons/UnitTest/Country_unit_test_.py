# Python class for unit test of Country 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Country import Country
from services import Country_service as commons_country_service
country_service = commons_country_service.CountryService()

test_primary_key_1 = "BBB"


class TestDaoCountry(unittest.TestCase):

    def test_dao(self):

        print("--- test CountryPersistence ")

        entity = Country()
        # --- Key values
        entity.code = test_primary_key_1
        # --- Other values
        entity.name = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        country_service.delete(entity)
        cpt_initial = country_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        country_service.insert(entity)
        self.assertTrue(country_service.exists_by_id(test_primary_key_1))
        self.assertTrue(country_service.exists(entity))

        cpt = country_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = country_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(country_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.name = "test_changement"
        element = country_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = country_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = country_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(country_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(country_service.delete(entity), 0)

        cpt_final = country_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(country_service.exists_by_id(test_primary_key_1))
        self.assertFalse(country_service.exists(entity))
        self.assertEqual(country_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

