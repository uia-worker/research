'''
Example is based on http://pythontesting.net/framework/unittest/unittest-introduction/
'''

import unittest
from mymodule import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 12)
    def test_string_a_b(self):
        self.assertEqual(add('5', '7'), '57', 'Wrong result for add')
        with self.assertRaises(TypeError):
            add('5',3)
        
        
if __name__ == '__main__':
    unittest.main()