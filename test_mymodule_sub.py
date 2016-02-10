import unittest
from mymodule import sub

class TestSub(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_4_5(self):
        self.assertEqual(sub(4,5),1)

if __name__ == '__main__':
    unittest.main()
    