#!/usr/bin/env python3
""" a unittest module TestAccessNestedMap """
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """ Test cases for get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        test to check for correct output
        """
        # create a mock object for the request.get method
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        # calling get_json function
        result = get_json(test_url)
        # assert that requests.get was called only once with test_url arg
        mock_get.assert_called_once_with(test_url)
        # assert that result is equal to expected test_payload
        self.assertEqual(result, test_payload)
