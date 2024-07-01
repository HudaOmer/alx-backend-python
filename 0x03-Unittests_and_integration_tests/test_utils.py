#!/usr/bin/env python3
"""
0. Parameterize a unit test
1. Parameterize a unit test
2. Mock HTTP calls
3. Parameterize and patch
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    a class that inherits from unittest.TestCase
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        unit test for utils.access_nested_map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """
        unit test for utils.access_nested_map
        """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """
        test that utils.get_json returns the expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    """

    def test_memoize(self):
        """
        test that utils.get_json returns the expected result
        """

        class TestClass:
            """
            a class
            """

            def a_method(self):
                """
                a function
                """
                return 42

            @memoize
            def a_property(self):
                """
                function
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
