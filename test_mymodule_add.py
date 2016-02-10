import unittest
from mymodule import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 12)
    # Delvis hentet fra ...
    def test_string_a_b(self):
        self.assertEqual(add(int('3'), 3), 'a3')
        
        
if __name__ == '__main__':
    unittest.main()