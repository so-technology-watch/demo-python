# Python class for unit test of EmployeeGroup 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.EmployeeGroup import EmployeeGroup
from services import EmployeeGroup_service as commons_employeegroup_service
employeegroup_service = commons_employeegroup_service.EmployeeGroupService()

test_primary_key_1 = "AAA"
test_primary_key_2 = 100


class TestDaoEmployeeGroup(unittest.TestCase):

    def test_dao(self):

        print("--- test EmployeeGroupPersistence ")

        entity = EmployeeGroup()
        # --- Key values
        entity.employeeCode = test_primary_key_1
        entity.groupId = test_primary_key_2
        # --- Other values

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        employeegroup_service.delete(entity)
        cpt_initial = employeegroup_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        employeegroup_service.insert(entity)
        self.assertTrue(employeegroup_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertTrue(employeegroup_service.exists(entity))

        cpt = employeegroup_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = employeegroup_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(employeegroup_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        element = employeegroup_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = employeegroup_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = employeegroup_service.delete_by_id(test_primary_key_1, test_primary_key_2)
        self.assertEqual(element, 1)
        self.assertEqual(employeegroup_service.delete_by_id(test_primary_key_1, test_primary_key_2), False)
        self.assertEqual(employeegroup_service.delete(entity), 0)

        cpt_final = employeegroup_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(employeegroup_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertFalse(employeegroup_service.exists(entity))
        self.assertEqual(employeegroup_service.find_by_id(test_primary_key_1, test_primary_key_2), False)

        print("Normal end of persistence service test.")

