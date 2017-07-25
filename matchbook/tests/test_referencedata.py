
import unittest
import unittest.mock as mock

from matchbook.apiclient import APIClient
from matchbook.endpoints.referencedata import ReferenceData
from matchbook.enums import Side, MarketStates, Boolean


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.client = APIClient('username', 'password')
        self.reference_data = ReferenceData(self.client)

    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_currencies(self, mock_request, mock_process_response):
        self.reference_data.get_currencies()

        mock_request.assert_called_once_with("GET", self.client.urn_main, 'lookups/currencies', session=None,)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_sports(self, mock_request, mock_process_response):
        self.reference_data.get_sports()

        mock_request.assert_called_once_with("GET", self.client.urn_edge,  'lookups/sports',
                                             params={'order': 'name asc', 'per-page': 500}, session=None,)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_oddstype(self, mock_request, mock_process_response):
        self.reference_data.get_oddstype()

        mock_request.assert_called_once_with("GET", self.client.urn_main, 'lookups/odds-types', session=None,)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_countries(self, mock_request, mock_process_response):
        self.reference_data.get_countries()

        mock_request.assert_called_once_with("GET", self.client.urn_main, 'lookups/countries', session=None,)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_regions(self, mock_request, mock_process_response):
        self.reference_data.get_regions(country_id=1)

        mock_request.assert_called_once_with("GET", self.client.urn_main, 'lookups/regions/1', session=None,)
        assert mock_process_response.call_count == 1

    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.process_response')
    @mock.patch('matchbook.endpoints.referencedata.ReferenceData.request', return_value=mock.Mock())
    def test_get_navigation(self, mock_request, mock_process_response):
        self.reference_data.get_navigation()

        mock_request.assert_called_once_with(
            "GET", self.client.urn_edge, 'navigation', params={'offset': 0, 'per-page': 500}, session=None,
        )
        assert mock_process_response.call_count == 1
