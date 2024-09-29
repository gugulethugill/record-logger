import unittest
from record_manager import RecordManager  

class RecordManagerTests(unittest.TestCase):

    def setUp(self):
        self.record_manager = RecordManager()  # Create a new RecordManager instance for each test

    def test_add_record(self):
        self.record_manager.add_record("First Record")
        self.assertEqual(len(self.record_manager.records), 1)
        self.assertEqual(self.record_manager.records[0], "First Record")

    def test_get_last_record_with_records(self):
        self.record_manager.add_record("First Record")
        self.record_manager.add_record("Second Record")
        self.assertEqual(self.record_manager.get_last_record(), "Second Record")

    def test_get_last_record_no_records(self):
        self.assertIsNone(self.record_manager.get_last_record())

if __name__ == '__main__':
    unittest.main()
