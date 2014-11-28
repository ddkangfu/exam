#coding=utf-8


import unittest
from converter import string_to_long

class ConverterTest(unittest.TestCase):
    def test_number_string_without_sign(self):
        expect = 123456
        result = string_to_long('123456')
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
