#!/usr/bin/env python3
""" unittest module """
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ test cases for GithubOrgClient """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ check for correct output """
        # instantiate the GithubOrgClient with provided org name
        github_org_client = GithubOrgClient(org_name)

        # call the org method
        result = github_org_client.org

        # assert get_json was onlhy called once
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/{}".
                                              format(org_name))
