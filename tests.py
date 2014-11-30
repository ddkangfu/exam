#coding=utf-8

import unittest

from converter import string_to_long
from tri_nary_tree import TriNaryTree


class ConverterTestCase(unittest.TestCase):
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

    def test_blank_number_string(self):
        expect = "invalid literal for string_to_long() with base 10: ''"
        err_message = ''

        try:
            result = string_to_long('')
        except ValueError, ex:
            err_message = ex.message
        self.assertEqual(err_message, expect)

    def test_non_numeric_string(self):
        expect = "invalid literal for string_to_long() with base 10: 'abc'"
        err_message = ''

        try:
            result = string_to_long('abc')
        except ValueError, ex:
            err_message = ex.message
        self.assertEqual(err_message, expect)

    def test_number_string_with_none_value(self):
        expect = "invalid literal for string_to_long() with base 10: 'None'"
        err_message = ''

        try:
            result = string_to_long(None)
        except ValueError, ex:
            err_message = ex.message
        self.assertEqual(err_message, expect)

    def test_number_string_with_a_space_character(self):
        expect = "invalid literal for string_to_long() with base 10: ' '"
        err_message = ''

        try:
            result = string_to_long(' ')
        except ValueError, ex:
            err_message = ex.message
        self.assertEqual(err_message, expect)

    def test_number_string_with_a_space_character_as_prefix(self):
        expect = 123456
        result = string_to_long(' 123456')
        self.assertEqual(result, expect)


class TriNaryTreeTaseCase(unittest.TestCase):
    def test_insert_one_node(self):
        expect = "[5]"
        tree = TriNaryTree()
        tree.insert(5)
        self.assertEqual(tree.__str__(), expect)


if __name__ == '__main__':
    unittest.main()
