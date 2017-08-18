import unittest
import datetime

from entities.Review import Review
from services import Review_service as commons_review_service
review_service = commons_review_service.ReviewService("Review")

test_primary_key_1 = "AAA"
test_primary_key_2 = 100


class TestDaoReview(unittest.TestCase):

    def test_dao(self):

        print("--- test ReviewPersistence ")

        entity = Review()
        # --- Key values
        entity.customerCode = test_primary_key_1
        entity.bookId = test_primary_key_2
        # --- Other values
        entity.reviewText = "test_value"
        entity.reviewNote = 1
        entity.creation = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")
        entity.lastUpdate = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        review_service.delete(entity)
        cpt_initial = review_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        review_service.insert(entity)
        self.assertTrue(review_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertTrue(review_service.exists(entity))

        cpt = review_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = review_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        self.assertTrue(review_service.exists(entity))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.reviewText = "test_changement"
        entity.reviewNote = 2
        entity.creation = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        entity.lastUpdate = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        element = review_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, 1)

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = review_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(type(element), type(entity))
        self.assertEqual(element.to_dict(), entity.to_dict())
        print("Found : {}".format(element))

        # --- DELETE
        element = review_service.delete_by_id(test_primary_key_1, test_primary_key_2)
        self.assertEqual(element, 1)
        self.assertEqual(review_service.delete_by_id(test_primary_key_1, test_primary_key_2), False)
        self.assertEqual(review_service.delete(entity), 0)

        cpt_final = review_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(review_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertFalse(review_service.exists(entity))
        self.assertEqual(review_service.find_by_id(test_primary_key_1, test_primary_key_2), False)

        print("Normal end of persistence service test.")

