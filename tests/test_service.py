import unittest
import lob
# Setting the API key

class ServiceFunctions(unittest.TestCase):
    def setUp(self):
      lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_packaging_list(self):
        print lob.Packaging.list()

