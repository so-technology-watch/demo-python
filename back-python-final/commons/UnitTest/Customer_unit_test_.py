# Python class for unit test of Customer 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Customer import Customer
from services import Customer_service as commons_customer_service
customer_service = commons_customer_service.CustomerService()

test_primary_key_1 = "BBB"


class TestDaoCustomer(unittest.TestCase):

    def test_dao(self):

        print("--- test CustomerPersistence ")

        entity = Customer()
        # --- Key values
        entity.code = test_primary_key_1
        # --- Other values
        entity.countryCode = "AAA"
        entity.firstName = "test_value"
        entity.lastName = "test_value"
        entity.login = "test_value"
        entity.password = "test_value"
        entity.age = 1
        entity.city = "test_value"
        entity.zipCode = 1
        entity.phone = "test_value"
        entity.reviewer = 1

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        customer_service.delete(entity)
        cpt_initial = customer_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        customer_service.insert(entity)
        self.assertTrue(customer_service.exists_by_id(test_primary_key_1))
        self.assertTrue(customer_service.exists(entity))

        cpt = customer_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = customer_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(customer_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.firstName = "test_changement"
        entity.lastName = "test_changement"
        entity.login = "test_changement"
        entity.password = "test_changement"
        entity.age = 2
        entity.city = "test_changement"
        entity.zipCode = 2
        entity.phone = "test_changement"
        entity.reviewer = 2
        element = customer_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = customer_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = customer_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(customer_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(customer_service.delete(entity), 0)

        cpt_final = customer_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(customer_service.exists_by_id(test_primary_key_1))
        self.assertFalse(customer_service.exists(entity))
        self.assertEqual(customer_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

