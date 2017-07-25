
import unittest
import unittest.mock as mock

from matchbook.apiclient import APIClient
from matchbook.endpoints.reporting import Reporting
from matchbook.enums import TransactionCategories, TransactionTypes


class ReportingTest(unittest.TestCase):

    def setUp(self):
        self.client = APIClient('username', 'password')
        self.reporting = Reporting(self.client)

    @mock.patch('matchbook.endpoints.reporting.Reporting.process_response')
    @mock.patch('matchbook.endpoints.reporting.Reporting.request', return_value=mock.Mock())
    def test_get_old_transactions_report(self, mock_request, mock_process_response):
        self.reporting.get_old_transactions_report(offset=0, per_page=500, categories=TransactionCategories.Exchange)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_main, 'reports/transactions', target='transactions', session=None,
            params={'offset': 0, 'per-page': 500, 'categories': 'exchange'},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.reporting.Reporting.process_response')
    @mock.patch('matchbook.endpoints.reporting.Reporting.request', return_value=mock.Mock())
    def test_get_new_transactions_report(self, mock_request, mock_process_response):
        self.reporting.get_new_transactions_report(transaction_type=TransactionTypes.All, offset=0, per_page=500)

        mock_request.assert_called_once_with("GET", self.client.urn_edge, 'reports/v1/transactions',
                                             target='transactions', session=None, params={'offset': 0, 'per-page': 500})
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.reporting.Reporting.process_response')
    @mock.patch('matchbook.endpoints.reporting.Reporting.request', return_value=mock.Mock())
    def test_get_current_offers(self, mock_request, mock_process_response):
        self.reporting.get_current_offers(sport_ids='9', offset=0, per_page=500)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'reports/v1/offers/current', target='offers', session=None,
            params={'sport-ids': '9', 'offset': 0, 'per-page': 500})
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.reporting.Reporting.process_response')
    @mock.patch('matchbook.endpoints.reporting.Reporting.request', return_value=mock.Mock())
    def test_get_current_bets(self, mock_request, mock_process_response):
        self.reporting.get_current_bets(sport_ids='9', offset=0, per_page=500)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'reports/v1/bets/current', target='bets', session=None,
            params={'sport-ids': '9', 'offset': 0, 'per-page': 500})
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.reporting.Reporting.process_response')
    @mock.patch('matchbook.endpoints.reporting.Reporting.request', return_value=mock.Mock())
    def test_get_settled_bets(self, mock_request, mock_process_response):
        self.reporting.get_settled_bets(sport_ids='9', offset=0, per_page=500)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'reports/v1/bets/settled', target='bets', session=None,
            params={'sport-ids': '9', 'offset': 0, 'per-page': 500})
        assert mock_process_response.call_count == 1
