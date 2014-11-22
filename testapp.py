import os
import unittest
from app import app

class NBServeTestCase(unittest.TestCase):
    def testIndex(self):
        with app.test_client() as c:
            c.get('/')

    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()