# Python class for unit test of Employee 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Employee import Employee
from services import Employee_service as commons_employee_service
employee_service = commons_employee_service.EmployeeService()

test_primary_key_1 = "BBB"


class TestDaoEmployee(unittest.TestCase):

    def test_dao(self):

        print("--- test EmployeePersistence ")

        entity = Employee()
        # --- Key values
        entity.code = test_primary_key_1
        # --- Other values
        entity.shopCode = "AAA"
        entity.firstName = "test_value"
        entity.lastName = "test_value"
        entity.manager = 1
        entity.badgeNumber = 100	
        entity.email = "test_value"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        employee_service.delete(entity)
        cpt_initial = employee_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        employee_service.insert(entity)
        self.assertTrue(employee_service.exists_by_id(test_primary_key_1))
        self.assertTrue(employee_service.exists(entity))

        cpt = employee_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = employee_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(employee_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.firstName = "test_changement"
        entity.lastName = "test_changement"
        entity.manager = 2
        entity.email = "test_changement"
        element = employee_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = employee_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = employee_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(employee_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(employee_service.delete(entity), 0)

        cpt_final = employee_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(employee_service.exists_by_id(test_primary_key_1))
        self.assertFalse(employee_service.exists(entity))
        self.assertEqual(employee_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

