# Python class for unit test of Badge 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Badge import Badge
from services import Badge_service as commons_badge_service
badge_service = commons_badge_service.BadgeService()

test_primary_key_1 = 200


class TestDaoBadge(unittest.TestCase):

    def test_dao(self):

        print("--- test BadgePersistence ")

        entity = Badge()
        # --- Key values
        entity.badgeNumber = test_primary_key_1
        # --- Other values
        entity.authorizationLevel = 1
        entity.endOfValidity = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        badge_service.delete(entity)
        cpt_initial = badge_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        badge_service.insert(entity)
        self.assertTrue(badge_service.exists_by_id(test_primary_key_1))
        self.assertTrue(badge_service.exists(entity))

        cpt = badge_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = badge_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(badge_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.authorizationLevel = 2
        entity.endOfValidity = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        element = badge_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = badge_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = badge_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(badge_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(badge_service.delete(entity), 0)

        cpt_final = badge_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(badge_service.exists_by_id(test_primary_key_1))
        self.assertFalse(badge_service.exists(entity))
        self.assertEqual(badge_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

