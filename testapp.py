import unittest
import os
from app import app

class TestUpload(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        os.remove('uploads/test.jpg')

    def test_upload(self):
        with open('test.jpg', 'rb') as f:
            response = self.app.post('/upload', data={'file': f})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('uploads/test.jpg'))

if __name__ == '__main__':
    unittest.main()
