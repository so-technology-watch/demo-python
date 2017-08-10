import unittest

from commons.TestDaoUni import TestDao_service as commons_test_service
test_service = commons_test_service.TestDaoService("TestDao")


class TestDaoUnitaire(unittest.TestCase):

    def test_count(self):
        element = test_service.count_all()
        self.assertEqual(element, 0)

    def test_select_all(self):
        element = test_service.find_all()
        self.assertEqual(element, [])

    def test_select(self):
        element = test_service.find_by_id("TestDao.id == 1")
        self.assertEqual(element, {"entity": None, "code": 200})

    def test_insert(self):
        entity = {"id": 1, "name": "test_name"}
        element = test_service.insert(entity)
        self.assertEqual(element, {"code: 201"})

if __name__ == '__main__':
    unittest.main()