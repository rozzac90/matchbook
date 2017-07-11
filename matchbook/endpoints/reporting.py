
import datetime

from matchbook import resources
from matchbook.utils import clean_locals
from matchbook.endpoints.baseendpoint import BaseEndpoint
from matchbook.enums import TransactionCategories, TransactionTypes, PeriodFilter


class Reporting(BaseEndpoint):

    def get_old_transactions_report(self, offset=0, per_page=500, after=None, before=None, period=PeriodFilter.Default,
                                    categories=TransactionCategories.Exchange, session=None):
        """
        Get paginated historical transactions, filtered by arguments specified

        :param offset: starting point from which the paginated results begin. Default 0.
        :type offset: int
        :param per_page: number of bets to be returned per call, max 500. Default 20.
        :type per_page: int
        :param after: event start time lower cutoff. Default 0.
        :type after: UNIX timestamp
        :param before: event start time upper cutoff. Default current time.
        :type before: UNIX timestamp
        :param period: filter for the amount of time to include in settlement search.
        :type period: matchbook.enums.PeriodFilter
        :param categories: where the transaction was incurred, casino or exchange.
        :type categories: matchbook.enums.TransactionCategories
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Historical transaction info.
        :rtype: json
        :raises: matchbook.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request(
            'GET', self.client.urn_main, 'reports/transactions', params=params, target='transactions', session=session
        )
        return self.process_response(
            response, resources.TransactionReport,
            date_time_sent, datetime.datetime.now()
        )

    def get_new_transactions_report(self, transaction_type=TransactionTypes.All, offset=0, per_page=500, 
                                    after=None, before=None, session=None):
        # TODO: Map resource and get example data for data_structures
        """
        Get paginated historical transactions, filtered by arguments specified

        :param offset: starting point from which the paginated results begin. Default 0.
        :type offset: int
        :param per_page: number of bets to be returned per call, max 500. Default 20.
        :type per_page: int
        :param after: event start time lower cutoff. Default 0.
        :type after: UNIX timestamp
        :param before: event start time upper cutoff. Default current time.
        :type before: UNIX timestamp
        :param transaction_type: filter by type of transaction.
        :type transaction_type: matchbook.enums.TransactionTypes
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Historical transaction info.
        :rtype: json
        :raises: matchbook.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request(
            'GET', self.client.urn_edge, 'reports/v1/transactions', params=params,
            target='transactions', session=session
        )
        return self.process_response(response, resources.TransactionReport, date_time_sent, datetime.datetime.now())

    def get_current_offers(self, sport_ids=None, event_ids=None, market_ids=None, offset=0, per_page=500, session=None):
        """
        Get a list of current offers i.e. offers on markets yet to be settled.
        
        :param sport_ids: operate only on orders on specified sports.
        :type sport_ids: comma separated string
        :param event_ids: operate only on orders on specified events.
        :type event_ids: comma separated string
        :param market_ids: operate only on orders on specified markets.
        :type market_ids: comma separated string
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
        response = self.request(
            'GET', self.client.urn_edge, 'reports/v1/offers/current', params=params, target='offers', session=session
        )
        return self.process_response(response, resources.Order, date_time_sent, datetime.datetime.now())

    def get_current_bets(self, sport_ids=None, event_ids=None, market_ids=None, offset=0, per_page=500, session=None):
        """
        Get a list of current bets i.e. offers that have been matched on markets yet to be settled.
        
        :param sport_ids: operate only on orders on specified sports.
        :type sport_ids: comma separated string
        :param event_ids: operate only on orders on specified events.
        :type event_ids: comma separated string
        :param market_ids: operate only on orders on specified markets.
        :type market_ids: comma separated string
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
        response = self.request(
            'GET', self.client.urn_edge, 'reports/v1/bets/current', params=params, target='bets', session=session
        )
        return self.process_response(response, resources.BetReport, date_time_sent, datetime.datetime.now())

    def get_settled_bets(self, sport_ids=None, event_ids=None, market_ids=None, before=None, after=None,
                         offset=0, per_page=500, session=None):
        """
        Get a list of settled bets.
        
        :param sport_ids: operate only on bets on specified sports.
        :type sport_ids: comma separated string
        :param event_ids: operate only on bets on specified events.
        :type event_ids: comma separated string
        :param market_ids: operate only on bets on specified markets.
        :type market_ids: comma separated string
        :param after: event start time lower cutoff. Default None.
        :type after: UNIX timestamp
        :param before: event start time upper cutoff. Default None.
        :type before: UNIX timestamp
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
        response = self.request(
            'GET', self.client.urn_edge, 'reports/v1/bets/settled', params=params, target='bets', session=session
        )
        return self.process_response(response, resources.BetReport, date_time_sent, datetime.datetime.now())


