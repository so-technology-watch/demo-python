# Python class for unit test of Book 
# Created on 2017-08-25 ( Time 18:18:32 )

import unittest
import datetime

from entities.Book import Book
from services import Book_service as commons_book_service
book_service = commons_book_service.BookService()

test_primary_key_1 = 200


class TestDaoBook(unittest.TestCase):

    def test_dao(self):

        print("--- test BookPersistence ")

        entity = Book()
        # --- Key values
        entity.id = test_primary_key_1
        # --- Other values
        entity.publisherId = 100	
        entity.authorId = 100	
        entity.isbn = "test_value"
        entity.title = "test_value"
        entity.price = 1
        entity.quantity = 1
        entity.discount = 1
        entity.availability = 1
        entity.bestSeller = 1

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        book_service.delete(entity)
        cpt_initial = book_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        book_service.insert(entity)
        self.assertTrue(book_service.exists_by_id(test_primary_key_1))
        self.assertTrue(book_service.exists(entity))

        cpt = book_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = book_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(book_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.isbn = "test_changement"
        entity.title = "test_changement"
        entity.price = 2
        entity.quantity = 2
        entity.discount = 2
        entity.availability = 2
        entity.bestSeller = 2
        element = book_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = book_service.find_by_id(test_primary_key_1)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = book_service.delete_by_id(test_primary_key_1)
        self.assertEqual(element, 1)
        self.assertEqual(book_service.delete_by_id(test_primary_key_1), False)
        self.assertEqual(book_service.delete(entity), 0)

        cpt_final = book_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(book_service.exists_by_id(test_primary_key_1))
        self.assertFalse(book_service.exists(entity))
        self.assertEqual(book_service.find_by_id(test_primary_key_1), False)

        print("Normal end of persistence service test.")

