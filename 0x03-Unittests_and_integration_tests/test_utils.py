#!/usr/bin/env python3
""" a unittest module TestAccessNestedMap """
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    nested map testing class
    """
    # using @parameterized.expand to define multiple test cases
    # with different inputs
    @parameterized.expand([
        # test case 1: single level nested map
        ({"a": 1}, ("a",), 1),
        # two-level nested map
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        # two-level nested map, accessing two keys
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test method for the correct output """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    # test cases for exception handling
    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         exception, expected_except_message):
        """ test for exceptions in the access_nested_map """
        with self.assertRaises(exception) as context:
            access_nested_map(nested_map, path)
        self.assertIn(expected_except_message, str(context.exception))
