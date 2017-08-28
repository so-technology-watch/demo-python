# Python class for unit test of Workgroup 
# Created on 2017-08-25 ( Time 18:18:33 )

import unittest
import datetime

from entities.Workgroup import Workgroup
from services import Workgroup_service as commons_workgroup_service
workgroup_service = commons_workgroup_service.WorkgroupService()

test_primary_key_1 = 200


class TestDaoWorkgroup(unittest.TestCase):

    def test_dao(self):

        print("--- test WorkgroupPersistence ")

        entity = Workgroup()
        # --- Key values
        entity.id = test_primary_key_1
        # --- Other values
        entity.name = "test_value"
        entity.description = "test_value"
        entity.creationDate = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        workgroup_service.delete(entity)
        cpt_initial = workgroup_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        workgroup_service.insert(entity)
        self.assertTrue(workgroup_service.exists_by_id(test_primary_key_1))
        self.assertTrue(workgroup_service.exists(entity))

        cpt = workgroup_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = workgroup_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(workgroup_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.name = "test_changement"
        entity.description = "test_changement"
        entity.creationDate = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        element = workgroup_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = workgroup_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = workgroup_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(workgroup_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(workgroup_service.delete(entity), 0)

        cpt_final = workgroup_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(workgroup_service.exists_by_id(test_primary_key_1))
        self.assertFalse(workgroup_service.exists(entity))
        self.assertEqual(workgroup_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

