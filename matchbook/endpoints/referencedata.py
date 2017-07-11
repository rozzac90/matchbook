import datetime

from matchbook.utils import clean_locals
from matchbook.endpoints.baseendpoint import BaseEndpoint
from matchbook import resources
from matchbook.enums import SportsOrder, MarketStates


class ReferenceData(BaseEndpoint):

    def get_currencies(self, session=None):
        """
        Get the accepted currencies on betting platform.
        
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Supported currencies.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_main, 'lookups/currencies', session=session)
        return self.process_response(
            response.json().get('currencies', []), resources.Currencies, date_time_sent, datetime.datetime.utcnow()
        )

    def get_sports(self, status=MarketStates.All, order=SportsOrder.NameAsc, session=None):
        """
        Lookup all sports, filter for active only/all.

        :param status: filter results by sport status, default 'active'.
        :type status: MatchbookAPI.bin.enums.SportStatus
        :param order: order in which results are returned, default 'name asc'.
        :type order: MatchbookAPI.bin.enums.SportsOrder
        :param session: requests session to be used.
        :type session: requests.Session
        :return: Sports that are active on the betting platform.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_edge, 'lookups/sports', params=params, session=session)
        return self.process_response(
            response.json().get('sports', []), resources.SportsDetails, date_time_sent, datetime.datetime.utcnow()
        )

    def get_oddstype(self, session=None):
        """
        Get the accepted odds-types.

        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Supported odds-types.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_main, 'lookups/odds-types', session=session)
        return self.process_response(
            response.json().get('odds-types', []), resources.OddsType, date_time_sent, datetime.datetime.utcnow()
        )

    def get_countries(self, session=None):
        """
        Get the countries and their relevant codes and ids.

        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Countries and their details.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_main, 'lookups/countries', session=session)
        return self.process_response(
            response.json().get('countries', []), resources.Countries, date_time_sent, datetime.datetime.utcnow()
        )

    def get_regions(self, country_id, session=None):
        """
        Get regions for a given country and their relevant codes and ids.

        :param country_id: id of the country whose regions we want to get.
        :type country_id: int
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Countries and their details.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_main, 'lookups/regions/%s' % country_id, session=session)
        return self.process_response(
            response.json().get('countries', []), resources.Regions, date_time_sent, datetime.datetime.utcnow()
        )

    def get_navigation(self, offset=0, per_page=500, session=None):
        # TODO: Map meta-tags to a resource.
        """
        Get page navigation tree breakdown.

        :param offset: starting point of results. Default 0.
        :type offset: int
        :param per_page: no. of offers returned in a single response, Max 500. Default 20.
        :type per_page: int
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Orders data
        :raises: MatchbookAPI.bin.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_edge, 'navigation', params=params, session=session)
        return self.process_response(
            response.json().get('countries', []), resources.MetaTags, date_time_sent, datetime.datetime.utcnow()
        )
