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

    def test_number_string_with_a_space_character_as_prefix(self):
        expect = 123456
        result = string_to_long(' 123456')
        self.assertEqual(result, expect)

    def test_blank_number_string(self):
        expect = "invalid literal for string_to_long() with base 10: ''"
        err_message = self._get_exception_message('')
        self.assertEqual(err_message, expect)

    def test_non_numeric_string(self):
        expect = "invalid literal for string_to_long() with base 10: 'abc'"
        err_message = self._get_exception_message('abc')
        self.assertEqual(err_message, expect)

    def test_number_string_with_none_value(self):
        expect = "invalid literal for string_to_long() with base 10: 'None'"
        err_message = self._get_exception_message('None')
        self.assertEqual(err_message, expect)

    def test_number_string_with_a_space_character(self):
        expect = "invalid literal for string_to_long() with base 10: ' '"
        err_message = self._get_exception_message(' ')
        self.assertEqual(err_message, expect)

    def _get_exception_message(self, value):
        except_msg = ''

        try:
            result = string_to_long(value)
        except ValueError, ex:
            except_msg = ex.message
        return except_msg


class TriNaryTreeTaseCase(unittest.TestCase):
    def test_insert_one_node(self):
        expect = [5]
        tree = TriNaryTree()
        tree.insert(5)
        self.assertEqual(str(tree), str(expect))

    def test_insert_multiple_node(self):
        expect = [5, 4, 2, 2, 5, 9, 7]
        tree = self._create_tree([5, 4, 9, 5, 7, 2, 2])
        self.assertEqual(str(tree), str(expect))
    
    def test_delete_root_node_without_middle_node(self):
        expect = [7, 4, 2, 2, 9]
        tree = self._create_tree([5, 4, 9, 7, 2, 2])
        tree.delete(5)
        self.assertEqual(str(tree), str(expect))
    
    def test_delete_root_node_with_middle_node(self):
        expect = [5, 4, 2, 2, 9, 7]
        tree = self._create_tree([5, 4, 9, 5, 7, 2, 2])
        tree.delete(5)
        self.assertEqual(str(tree), str(expect))
        
    def test_delete_leaf_node_on_the_left(self):
        expect = [5, 4, 2, 2, 5, 9]
        tree = self._create_tree([5, 4, 9, 5, 7, 2, 2])
        tree.delete(7)
        self.assertEqual(str(tree), str(expect))

    def test_delete_node_on_the_left(self):
        expect = [5, 2, 2, 5, 9, 7]
        tree = self._create_tree([5, 4, 9, 5, 7, 2, 2])
        tree.delete(4)
        self.assertEqual(str(tree), str(expect))        
    
    def test_delte_leaf_node_on_the_right(self):
        expect = [5, 4, 2, 2, 5, 9]
        tree = self._create_tree([5, 4, 9, 5, 11, 2, 2])
        tree.delete(11)
        self.assertEqual(str(tree), str(expect))                
    
    def test_delte_node_on_the_right(self):
        expect = [5, 4, 2, 2, 5, 7]
        tree = self._create_tree([5, 4, 9, 5, 7, 2, 2])
        tree.delete(9)
        self.assertEqual(str(tree), str(expect))

    def test_delete_inexist_node(self):
        expect = [5, 4, 2, 2, 5, 9, 7]
        tree = self._create_tree([5, 4, 9, 5, 7, 2, 2])
        tree.delete(11)
        self.assertEqual(str(tree), str(expect))

    def _create_tree(self, data):
        if not data:
            return None

        tree = TriNaryTree()
        for number in data:
            tree.insert(number)
        return tree


if __name__ == '__main__':
    unittest.main()
