#!/usr/bin/env python3
""" unittest module """
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ("example_url", {'repos_url': 'http://example.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ test case for _public_repos_url """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url):
        """ test for public_repos method """
        mock_public_repos_url.return_value = "example_url"

        with patch('client.get_json', return_value=[{"name": "repo1"},
                                                    {"name": "repo2"}]):
            instance = GithubOrgClient('test')
            result = instance.public_repos()

        expected_result = ["repo1", "repo2"]
        mock_public_repos_url.assert_called_once()
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ test for has_license method """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    test IntegrationGithubOrgClient
    """

    @classmethod
    def setUpClass(cls):
        """ set up the class with mocked requests.get """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # configure the side_effect for requests.get(url).json()
        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload),
        ]

    @classmethod
    def tearDownClass(cls):
        """ tear down the class and stop the patcher """
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """ Integration test for GithubOrgClient.public_repos """
        org_client = GithubOrgClient('test')

        result = org_client.public_repos()

        self.assertEqual(result, self.expected_repos)
