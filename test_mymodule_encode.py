import unittest
from mymodule import encode

class TestCode(unittest.TestCase):
    def setUp(self):
        pass
    def test_encode_shakespear(self):
        self.assertEqual(encode("to"),[1,2])

if __name__ == '__main__':
    unittest.main()