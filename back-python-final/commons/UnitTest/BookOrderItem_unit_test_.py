# Python class for unit test of BookOrderItem 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.BookOrderItem import BookOrderItem
from services import BookOrderItem_service as commons_bookorderitem_service
bookorderitem_service = commons_bookorderitem_service.BookOrderItemService()

test_primary_key_1 = 100
test_primary_key_2 = 100


class TestDaoBookOrderItem(unittest.TestCase):

    def test_dao(self):

        print("--- test BookOrderItemPersistence ")

        entity = BookOrderItem()
        # --- Key values
        entity.bookOrderId = test_primary_key_1
        entity.bookId = test_primary_key_2
        # --- Other values
        entity.quantity = 1
        entity.price = 1

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        bookorderitem_service.delete(entity)
        cpt_initial = bookorderitem_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        bookorderitem_service.insert(entity)
        self.assertTrue(bookorderitem_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertTrue(bookorderitem_service.exists(entity))

        cpt = bookorderitem_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = bookorderitem_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(bookorderitem_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.quantity = 2
        entity.price = 2
        element = bookorderitem_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = bookorderitem_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = bookorderitem_service.delete_by_id(test_primary_key_1, test_primary_key_2)
        self.assertEqual(element, 1)
        self.assertEqual(bookorderitem_service.delete_by_id(test_primary_key_1, test_primary_key_2), False)
        self.assertEqual(bookorderitem_service.delete(entity), 0)

        cpt_final = bookorderitem_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(bookorderitem_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertFalse(bookorderitem_service.exists(entity))
        self.assertEqual(bookorderitem_service.find_by_id(test_primary_key_1, test_primary_key_2), False)

        print("Normal end of persistence service test.")

