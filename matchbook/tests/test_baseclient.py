
import os
import unittest
import requests

from matchbook.baseclient import BaseClient
from matchbook.exceptions import PasswordError


class BaseClientTest(unittest.TestCase):

    def test_baseclient_init(self):
        client = BaseClient(username='username', password='password')
        assert client.username == 'username'
        assert client.password == 'password'
        assert client.url == 'https://matchbook.com'
        assert client.url_beta == 'https://beta.matchbook.com'
        assert client.urn_main == '/bpapi/rest/'
        assert client.urn_edge == '/edge/rest/'
        assert isinstance(client.session, requests.Session)
        assert client.headers == {'Content-Type': 'application/json', 'Accept': 'application/json'}
        assert client.exchange_type == 'back-lay'
        assert client.currency == 'EUR'

    def test_get_password(self):
        if 'MATCHBOOK_PW' in os.environ:
            client = BaseClient(username='username')
            assert client.password == os.environ['MATCHBOOK_PW']
        else:
            with self.assertRaises(PasswordError):
                BaseClient(username='username')

    def test_session_token(self):
        client = BaseClient(username='username', password='password')
        client.set_session_token(session_token='session_token', user_id=1234)
        assert client.session_token == 'session_token'
        assert client.user_id == 1234
