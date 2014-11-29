#coding=utf-8


import unittest
from converter import string_to_long

class ConverterTest(unittest.TestCase):
    def test_number_string_without_sign(self):
        expect = 123456
        result = string_to_long('123456')
        self.assertEqual(result, expect)

    def test_number_string_equal_zero(self):
        expect = 0
        result = string_to_long('0')
        self.assertEqual(result, expect)

    def test_number_string_with_positive_sign(self):
        expect = 123456
        result = string_to_long('+123456')
        self.assertEqual(result, expect)

    def test_number_string_with_negative_sign(self):
        expect = -654321
        result = string_to_long('-654321')
        self.assertEqual(result, expect)        


if __name__ == '__main__':
    unittest.main()
