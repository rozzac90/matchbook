
import datetime

from matchbook import resources
from matchbook.endpoints.baseendpoint import BaseEndpoint
from matchbook.enums import Boolean, Side, MarketNames, MarketType, MarketStates
from matchbook.utils import clean_locals


class MarketData(BaseEndpoint):

    def get_events(self, event_id=None, before=None, after=None, sport_ids=None, category_ids=None,
                   states=MarketStates.All, tag_url_names=None, per_page=500, offset=0,
                   include_event_participants=Boolean.T, price_depth=3, side=Side.All,
                   minimum_liquidity=None, session=None):
        """
        Get paginated events. Results can be filtered using various different parameters.

        :param event_id: specific event id. Default None.
        :type event_id: int
        :param after: event start time lower cutoff. Default None.
        :type after: UNIX timestamp
        :param before: event start time upper cutoff. Default None.
        :type before: UNIX timestamp
        :param category_ids: filter results by category id. Default None.
        :type category_ids: comma separated string
        :param sport_ids: filter results by sports id(s). Default None.
        :type sport_ids: comma separated string
        :param states: filter results by event state  or comma separated string of types. Default None.
        :type states: matchbook.enums.MarketStates
        :param tag_url_names:Only events with tags having url-name in the provided list are included in the response.
        :type tag_url_names: comma separated string
        :param per_page: number of results to show in a single result. Max=500. Default 20.
        :type per_page: int
        :param offset: starting page of results to show. Default 0.
        :type offset: int
        :param include_event_participants: A boolean indicating whether to return the event participants information
        :type include_event_participants: matchbook.enums.Boolean
        :param price_depth: max depth to be returned for prices. Default 3.
        :type price_depth: int
        :param side: filter results by side (dependent on exchange-type). Default None.
        :type side: matchbook.enums.Side
        :param minimum_liquidity: Only prices with available-amount greater than or equal to this value are included.
        :type minimum_liquidity: float
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Breakdown to each runner if they are included.
        :rtype: json
        :raises: matchbook.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        method = 'events'
        params['odds-type'] = self.client.odds_type
        params['exchange-type'] = self.client.exchange_type
        params['currency'] = self.client.currency
        if event_id:
            method = 'events/%s' % event_id
            del_keys = ['event-id', 'after', 'before', 'category-ids', 'sport-ids',
                        'states', 'per-page', 'offset', 'tag-url-names']
            params = {k: v for k, v in params.items() if k not in del_keys}
            response = self.request("GET", self.client.urn_edge, method, params=params, session=session)
            response = response.json().get('event', response.json())
        else:
            response = self.request(
                "GET", self.client.urn_edge, method, params=params, target='events', session=session
            )
        return self.process_response(response, resources.Event, date_time_sent, datetime.datetime.utcnow())

    def get_markets(self, event_id, market_id=None, names=MarketNames.All, types=MarketType.All, offset=0, per_page=500,
                    states=MarketStates.All, price_depth=3, side=Side.Default, minimum_liquidity=None, session=None):
        """
        Get paginated markets for an event specified by the event_id.

        :param event_id: specific event id.
        :type event_id: int
        :param market_id: specific market id to pull data for.
        :type market_id: int
        :param states: filter results by market state or a comma separated string of states. Default 'open', 'suspended'
        :type states: matchbook.enums.MarketStates
        :param types: filter results by market type or a comma separated string of types. Default None.
        :type types: matchbook.enums.MarketType
        :param names: filter results by market name. Default None.
        :type names: matchbook.enums.MarketNames
        :param per_page: number of results to show in a single result. Max=500. Default 20.
        :type per_page: int
        :param offset: starting page of results to show. Default 0.
        :type offset: int
        :param price_depth: max depth to be returned for prices. Default 3.
        :type price_depth: int
        :param side: filter results by side (dependent on exchange-type). Default None.
        :type side: matchbook.enums.Side
        :param minimum_liquidity: Only prices with available-amount greater than or equal to this value are included.
        :type minimum_liquidity: float
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Breakdown of each runner if they are included.
        :rtype: json
        :raises: matchbook.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        params['odds-type'] = self.client.odds_type
        params['exchange-type'] = self.client.exchange_type
        params['currency'] = self.client.currency
        method = 'events/%s/markets' % event_id
        if market_id:
            method = 'events/%s/markets/%s' % (event_id, market_id)
            del_keys = ['names', 'types', 'per-page', 'offset', 'states']
            params = {k: v for k, v in params.items() if k not in del_keys}
            response = self.request('GET', self.client.urn_edge, method, params=params, session=session)
            response = response.json().get('market', response.json())
        else:
            response = self.request(
                "GET", self.client.urn_edge, method, params=params, target='markets', session=session
            )
        return self.process_response(response, resources.Market, date_time_sent, datetime.datetime.utcnow())

    def get_runners(self, event_id, market_id, runner_id=None, states=MarketStates.All, include_withdrawn=Boolean.T,
                    include_prices=Boolean.T, price_depth=3, side=Side.All, minimum_liquidity=None, session=None):
        """
        Get runner data for an event and market specified by their ids.

        :param event_id: specific event id.
        :type event_id: int
        :param market_id: specific market id to pull data for.
        :type market_id: int
        :param runner_id: specific runner to pull data for.
        :type runner_id: int
        :param states: filter results by runner state or a comma separated string of states. Default 'open', 'suspended'
        :param include_withdrawn: boolean for returning or not the withdrawn runners in the response.
        :type include_withdrawn: matchbook.enums.Boolean
        :param include_prices: boolean indicating whether to return the prices for the runners.
        :type include_prices: matchbook.enums.Boolean
        :type states: matchbook.enums.MarketStates
        :param price_depth: max depth to be returned for prices. Default 3.
        :type price_depth: int
        :param side: filter results by side (dependent on exchange-type). Default None.
        :type side: matchbook.enums.Side
        :param minimum_liquidity: Only prices with available-amount greater than or equal to this value are included.
        :type minimum_liquidity: float
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Breakdown of each runner if they are included.
        :rtype: json
        :raises: matchbook.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        params['odds-type'] = self.client.odds_type
        params['exchange-type'] = self.client.exchange_type
        params['currency'] = self.client.currency
        method = 'events/%s/markets/%s/runners' % (event_id, market_id)
        if runner_id:
            method = 'events/%s/markets/%s/runners/%s' % (event_id, market_id, runner_id)
            del_keys = ['include-withdraw', 'states']
            params = {k: v for k, v in params.items() if k not in del_keys}
            response = self.request('GET', self.client.urn_edge, method, params=params, session=session)
            response = response.json().get('runner', response.json())
        else:
            response = self.request(
                'GET', self.client.urn_edge, method, params=params, target='runners', session=session
            )
        return self.process_response(response, resources.Runner, date_time_sent, datetime.datetime.utcnow())

    def get_popular_markets(self, price_depth=3, side=Side.All, minimum_liquidity=None,
                            old_format=Boolean.F, session=None):
        """
        Get popular markets as defined by matchbook.

        :param price_depth: max depth to be returned for prices. Default 3.
        :type price_depth: int
        :param side: filter results by side (dependent on exchange-type). Default None.
        :type side: matchbook.enums.Side
        :param minimum_liquidity: Only prices with available-amount greater than or equal to this value are included.
        :type minimum_liquidity: float
        :param old_format:
        :type old_format:
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Breakdown of each runner if they are included.
        :rtype: json
        :raises: matchbook.exceptions.ApiError
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        params['odds-type'] = self.client.odds_type
        params['exchange-type'] = self.client.exchange_type
        params['currency'] = self.client.currency
        response = self.request('GET', self.client.urn_edge, 'popular-markets', params=params, session=session)
        return self.process_response(
            response.json().get('markets', response.json()), resources.Market,
            date_time_sent, datetime.datetime.utcnow()
        )