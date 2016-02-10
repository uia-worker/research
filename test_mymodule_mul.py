import unittest
from mymodule import mul

class TestMul(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_4_5(self):
        self.assertEqual(mul(4,5),20)

if __name__ == '__main__':
    unittest.main()