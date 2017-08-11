import unittest
import datetime

from entities.Note import Note
from services import Note_service as commons_note_service
note_service = commons_note_service.NoteService("Note")

test_primary_key_1 = 100
test_primary_key_2 = 100


class TestDaoNote(unittest.TestCase):

    def test_dao(self):

        # --- Init table
        init = Note()
        init.idCours = 100
        init.idEleve = 100
        init.noteObtenue = 1
        init.dateExamen = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")
        init.codeMention = 100		

        print("--- test NotePersistence ")

        entity = Note()
        # --- Key values
        entity.idCours = test_primary_key_1
        entity.idEleve = test_primary_key_2
        # --- Other values
        entity.noteObtenue = 1
        entity.dateExamen = datetime.datetime.strptime("1011-11-11 00:00:00", "%Y-%m-%d %H:%M:%S")
        entity.codeMention = 100		

        # --- DELETE
        print("Delete : {}".format(entity.to_dict()))
        note_service.delete_by_id(test_primary_key_1, test_primary_key_2)
        cpt_initial = note_service.count_all()
        print("Initial count = {}".format(cpt_initial))

        # --- CREATE
        print("Create : {}".format(entity))
        element = note_service.insert(entity)
        self.assertEqual(element, {"code": 201})
        self.assertTrue(note_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertTrue(note_service.exists(entity))

        cpt = note_service.count_all()
        self.assertEqual(cpt, cpt_initial + 1)
        print("Count = {}".format(cpt))

        # --- FIND
        print("Find by id ...")
        element = note_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        self.assertTrue(note_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        print("Found : {}".format(element))

        # --- UPDATE
        # --- Change values
        entity.noteObtenue = 2
        entity.dateExamen = datetime.datetime.strptime("2022-02-22 00:00:00", "%Y-%m-%d %H:%M:%S")
        element = note_service.update(entity)
        print("Update : {}".format(entity))
        self.assertEqual(element, {"entity": entity, "code": 200})

        # --- RELOAD AFTER UPDATE
        print("Find by id ...")
        element = note_service.find_by_id(test_primary_key_1, test_primary_key_2)
        self.assertIsNotNone(element)
        self.assertEqual(element, {"entity": entity, "code": 200})
        print("Found : {}".format(element))

        # --- DELETE
        element = note_service.delete_by_id(test_primary_key_1, test_primary_key_2)
        self.assertEqual(element, {'entity': 1, 'code': 204})
        self.assertEqual(note_service.delete_by_id(test_primary_key_1, test_primary_key_2), {'entity': 0, 'code': 204})
        self.assertEqual(note_service.delete(entity), {'entity': 0, 'code': 204})

        cpt_final = note_service.count_all()
        self.assertEqual(cpt_final, cpt_initial)
        print("Final count = {}".format(cpt))

        self.assertFalse(note_service.exists_by_id(test_primary_key_1, test_primary_key_2))
        self.assertFalse(note_service.exists(entity))
        self.assertEqual(note_service.find_by_id(test_primary_key_1, test_primary_key_2), {"entity": None, "code": 200})

        print("Normal end of persistence service test.")

