import unittest
from mymodule import code

class TestCode(unittest.TestCase):
    def setUp(self):
        pass
    def test_table_entry_4(self):
        self.assertEqual(code()[4],'e')

if __name__ == '__main__':
    unittest.main()