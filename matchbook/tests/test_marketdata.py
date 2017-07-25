
import unittest
import unittest.mock as mock

from matchbook.apiclient import APIClient
from matchbook.endpoints.marketdata import MarketData
from matchbook.enums import Side, MarketStates, Boolean


class MarketDataTest(unittest.TestCase):

    def setUp(self):
        self.client = APIClient('username', 'password')
        self.market_data = MarketData(self.client)

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_events(self, mock_request, mock_process_response):
        self.market_data.get_events(sport_ids='9', states=MarketStates.All, per_page=500, offset=0,
                                    include_event_participants=Boolean.T, price_depth=3, side=Side.All)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'events', session=None, target='events',
            params={'sport-ids': '9', 'price-depth': 3, 'offset': 0, 'per-page': 500,
                    'exchange-type': self.client.exchange_type, 'include-event-participants': 'true',
                    'odds-type': self.client.odds_type, 'currency': self.client.currency},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_events_single(self, mock_request, mock_process_response):
        self.market_data.get_events(event_id=123, include_event_participants=Boolean.T, price_depth=3, side=Side.All)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'events/123', session=None,
            params={'price-depth': 3, 'exchange-type': self.client.exchange_type, 'include-event-participants': 'true',
                    'odds-type': self.client.odds_type, 'currency': self.client.currency},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_markets(self, mock_request, mock_process_response):
        self.market_data.get_markets(event_id=123, offset=0, per_page=500, price_depth=3)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'events/123/markets', session=None, target='markets',
            params={'event-id': 123, 'price-depth': 3, 'offset': 0, 'per-page': 500, 'currency': self.client.currency,
                    'exchange-type': self.client.exchange_type, 'odds-type': self.client.odds_type},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_markets_single(self, mock_request, mock_process_response):
        self.market_data.get_markets(event_id=123, market_id=345, offset=0, per_page=500, price_depth=3)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'events/123/markets/345', session=None,
            params={'event-id': 123, 'market-id': 345, 'price-depth': 3, 'currency': self.client.currency,
                    'exchange-type': self.client.exchange_type, 'odds-type': self.client.odds_type},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_runners(self, mock_request, mock_process_response):
        self.market_data.get_runners(event_id=123, market_id=345, include_withdrawn=Boolean.T, include_prices=Boolean.T,
                                     price_depth=3, side=Side.All)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'events/123/markets/345/runners', session=None, target='runners',
            params={'event-id': 123, 'market-id': 345, 'price-depth': 3, 'include-withdrawn': 'true',
                    'include-prices': 'true', 'currency': self.client.currency,
                    'exchange-type': self.client.exchange_type, 'odds-type': self.client.odds_type},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_runners_single(self, mock_request, mock_process_response):
        self.market_data.get_runners(event_id=123, market_id=345, runner_id=567, include_withdrawn=Boolean.T,
                                     include_prices=Boolean.T, price_depth=3)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'events/123/markets/345/runners/567', session=None,
            params={'event_id': 123, 'market-id': 345, 'runner-id': 567, 'price-depth': 3,
                    'include-prices': 'true', 'currency': self.client.currency, 'include-withdrawn': 'true',
                    'exchange-type': self.client.exchange_type, 'odds-type': self.client.odds_type},
        )
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.marketdata.MarketData.process_response')
    @mock.patch('matchbook.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_popular_markets(self, mock_request, mock_process_response):
        self.market_data.get_popular_markets(price_depth=3, old_format=Boolean.F)

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'popular-markets', session=None,
            params={'price-depth': 3, 'old-format': 'false', 'currency': self.client.currency,
                    'exchange-type': self.client.exchange_type, 'odds-type': self.client.odds_type},
        )
        assert mock_process_response.call_count == 1
