import unittest
from app import app, record_manager
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        record_manager.records = []  # Clear the records before each test

    def test_add_record_success(self):
        response = self.app.post('/record',
                                 data=json.dumps({"record": "Test Record"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Record added successfully", response.data)

    def test_add_record_missing_field(self):
        response = self.app.post('/record',
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing 'record' field", response.data)

    def test_get_last_record_success(self):
        self.app.post('/record',
                      data=json.dumps({"record": "Test Record"}),
                      content_type='application/json')
        response = self.app.get('/record')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Record", response.data)

    def test_get_last_record_empty(self):
        response = self.app.get('/record')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"No records found", response.data)

if __name__ == '__main__':
    unittest.main()