import unittest
import datetime

from entities.Shop import Shop
from services import Shop_service as commons_shop_service
shop_service = commons_shop_service.ShopService("Shop")

test_primary_key_1 = "BBB"


class TestDaoShop(unittest.TestCase):

    def test_dao(self):

        print("--- test ShopPersistence ")

        entity = Shop()
        # --- Key values
        entity.code = test_primary_key_1
        # --- Other values
        entity.name = "test_value"
        entity.address1 = "test_value"
        entity.address2 = "test_value"
        entity.zipCode = 1
        entity.city = "test_value"
        entity.countryCode = "AAA"
        entity.phone = "test_value"
        entity.email = "test_value"
        entity.executive = "AAA"

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        shop_service.delete(entity)
        cpt_initial = shop_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        shop_service.insert(entity)
        self.assertTrue(shop_service.exists_by_id(test_primary_key_1))
        self.assertTrue(shop_service.exists(entity))

        cpt = shop_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = shop_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(shop_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.name = "test_changement"
        entity.address1 = "test_changement"
        entity.address2 = "test_changement"
        entity.zipCode = 2
        entity.city = "test_changement"
        entity.phone = "test_changement"
        entity.email = "test_changement"
        element = shop_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = shop_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = shop_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(shop_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(shop_service.delete(entity), 0)

        cpt_final = shop_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(shop_service.exists_by_id(test_primary_key_1))
        self.assertFalse(shop_service.exists(entity))
        self.assertEqual(shop_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

