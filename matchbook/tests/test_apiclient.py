
import unittest

from matchbook.apiclient import APIClient
from matchbook.endpoints import Betting, Account, KeepAlive, Login, Logout, MarketData, ReferenceData, Reporting


class APIClientTest(unittest.TestCase):

    def test_apiclient_init(self):
        client = APIClient('username', 'password')
        assert str(client) == 'APIClient'
        assert repr(client) == '<APIClient [username]>'
        assert isinstance(client.account, Account)
        assert isinstance(client.betting, Betting)
        assert isinstance(client.keep_alive, KeepAlive)
        assert isinstance(client.login, Login)
        assert isinstance(client.logout, Logout)
        assert isinstance(client.market_data, MarketData)
        assert isinstance(client.reference_data, ReferenceData)
        assert isinstance(client.reporting, Reporting)
