
import unittest
import unittest.mock as mock

from matchbook.apiclient import APIClient
from matchbook.endpoints.account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.account = Account(client)

    @mock.patch('matchbook.endpoints.account.Account.process_response')
    @mock.patch('matchbook.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_account(self, mock_request, mock_process_response):
        self.account.get_account(balance_only=False)

        mock_request.assert_called_once_with("GET", '/edge/rest/', 'account', session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.account.Account.process_response')
    @mock.patch('matchbook.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_account_balance_only(self, mock_request, mock_process_response):
        self.account.get_account(balance_only=True)

        mock_request.assert_called_once_with("GET", '/edge/rest/', 'account/balance', session=None)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.account.Account.process_response')
    @mock.patch('matchbook.endpoints.account.Account.request', return_value=mock.Mock())
    def test_wallet_transfer(self, mock_request, mock_process_response):
        self.account.wallet_transfer(amount=10.0)

        mock_request.assert_called_once_with(
            "POST", '/bpapi/rest/', 'account/transfer', data={'amount': 10.0}, session=None
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.account.Account.process_response')
    @mock.patch('matchbook.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_casino_balance(self, mock_request, mock_process_response):
        self.account.get_casino_balance()

        mock_request.assert_called_once_with("GET", '/bpapi/rest/', 'account/balance', session=None)
        assert mock_process_response.call_count == 1
