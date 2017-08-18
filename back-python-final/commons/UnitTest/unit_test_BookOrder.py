import unittest
import datetime

from entities.BookOrder import BookOrder
from services import BookOrder_service as commons_bookorder_service
bookorder_service = commons_bookorder_service.BookOrderService("BookOrder")

test_primary_key_1 = 200


class TestDaoBookOrder(unittest.TestCase):

    def test_dao(self):

        print("--- test BookOrderPersistence ")

        entity = BookOrder()
        # --- Key values
        entity.id = test_primary_key_1
        # --- Other values
        entity.shopCode = "AAA"
        entity.customerCode = "AAA"
        entity.employeeCode = "AAA"
        entity.date = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")
        entity.state = 1

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        bookorder_service.delete(entity)
        cpt_initial = bookorder_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        bookorder_service.insert(entity)
        self.assertTrue(bookorder_service.exists_by_id(test_primary_key_1))
        self.assertTrue(bookorder_service.exists(entity))

        cpt = bookorder_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = bookorder_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(bookorder_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.date = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        entity.state = 2
        element = bookorder_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = bookorder_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = bookorder_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(bookorder_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(bookorder_service.delete(entity), 0)

        cpt_final = bookorder_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(bookorder_service.exists_by_id(test_primary_key_1))
        self.assertFalse(bookorder_service.exists(entity))
        self.assertEqual(bookorder_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

