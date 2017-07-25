
import unittest
import unittest.mock as mock

from matchbook.apiclient import APIClient
from matchbook.endpoints.betting import Betting
from matchbook.enums import Side, Status, AggregationType


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.client = APIClient('username', 'password')
        self.betting = Betting(self.client)

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_orders(self, mock_request, mock_process_response):
        self.betting.get_orders(event_ids=None, market_ids=None, runner_ids=None, offer_id=None, offset=0, per_page=500,
                                interval=None, side=Side.Default, status=Status.Default, session=None)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'offers', session=None, target='offers',
            params={'offset': 0, 'per-page': 500, 'exchange-type': self.client.exchange_type},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_orders_single(self, mock_request, mock_process_response):
        self.betting.get_orders(event_ids=None, market_ids=None, runner_ids=None, offer_id=123, offset=0, per_page=500,
                                interval=None, side=Side.Default, status=Status.Default, session=None)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'offers/123', session=None, params={'odds-type': self.client.odds_type}
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_send_orders(self, mock_request, mock_process_response):
        self.betting.send_orders(runner_id=1111, odds=2.0, side=Side.Back, stake=10.0, temp_id=None, session=None)

        mock_request.assert_called_once_with(
            "POST", self.client.urn_edge, 'offers', session=None,
            data={'offers': [{'runner-id': 1111, 'side': 'back', 'stake': 10.0, 'odds': 2.0, 'temp-id': None}],
                    'odds-type': self.client.odds_type,
                    'exchange-type': self.client.exchange_type,
                    'currency': self.client.currency}
        )
        assert mock_process_response.call_count == 1


    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_aggregate_bets(self, mock_request, mock_process_response):
        self.betting.get_agg_matched_bets(event_ids='1,2,3', market_ids=None, runner_ids=None, side=None, offset=0,
                                          per_page=500, aggregation_type=AggregationType.Default, session=None)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'bets/matched/aggregated', session=None, target='bets',
            params={'event-ids': '1,2,3', 'per-page': 500, 'offset': 0, 'aggregation-type': 'average'}
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_positions(self, mock_request, mock_process_response):
        self.betting.get_positions(
            event_ids=None, market_ids='1,2', runner_ids=None, offset=0, per_page=500, session=None
        )

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'accounts/positions', session=None,
            params={'market-ids': '1,2', 'per-page': 500, 'offset': 0}
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_amend_orders(self, mock_request, mock_process_response):
        self.betting.amend_orders(
            order_id=[1111, 1112], odds=[2.0, 1.9], side=[Side.Back, Side.Lay], stake=[10.0, 10.0], session=None
        )

        mock_request.assert_called_once_with(
            "PUT", self.client.urn_edge, 'offers', session=None,
            data={'offers': [{'id': 1111, 'side': 'back', 'stake': 10.0, 'odds': 2.0},
                             {'id': 1112, 'side': 'lay', 'stake': 10.0, 'odds': 1.9}],
                  'odds-type': self.client.odds_type,
                  'exchange-type': self.client.exchange_type,
                  'currency': self.client.currency}
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_delete_bulk_orders(self, mock_request, mock_process_response):
        self.betting.delete_bulk_orders(market_ids='142,152342')

        mock_request.assert_called_once_with(
            "DELETE", self.client.urn_edge, 'offers', session=None, data={'market-ids': '142,152342'},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.betting.Betting.process_response')
    @mock.patch('matchbook.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_delete_order(self, mock_request, mock_process_response):
        self.betting.delete_order(offer_id=1234)

        mock_request.assert_called_once_with("DELETE", self.client.urn_edge, 'offers/1234', session=None)
        assert mock_process_response.call_count == 1
