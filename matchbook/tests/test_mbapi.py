
import os
from unittest import TestCase
from matchbook.apiclient import APIClient


class TestMatchbook(TestCase):
    api = APIClient(
        username=os.environ['MATCHBOOK_USERNAME'],
        password=os.environ['MATCHBOOK_PW']
    )
    api.login()

    def test_settled(self):
        settled = self.api.reporting.get_settlement_bets()
        print(settled)

    def test_navigation(self):
        nav = self.api.reference_data.get_navigation()
        assert nav

    def test_send_order(self):
        # self.api.send_orders(
            # runner_id=432346050920009,
            # odds=3.5,
            # side='BACK',
            # stake=10,
            # temp_id=''
        # )
        return

    def test_get_prices(self):
        tennis_markets = self.api.market_data.get_events(sport_ids=[9])
        top_event = sorted(tennis_markets, key=lambda x: x['volume'], reverse=True)[0]
        event_id = top_event['id']
        market_id = next(mkt['id'] for mkt in top_event['markets'] if mkt['market-type'] == 'money_line')
        self.api.market_data.get_markets(event_id, market_id)

    def test_get_sports(self):
        sports = self.api.reference_data.get_sports()
        assert sports

    def test_send_quotes(self):
        order_list = [
            {'market_id': '450147584000010', 'order_type': 'GFD', 'timestamp': 1491008502, 'credit': 0, 'channel_type': 'matchbook',
            'side': 'back', 'size': 55.0, 'runner_id': 450147584080010, 'runner': 'Utah Jazz', 'price': 1.81},
            {'market_id': '450147584000010', 'order_type': 'GFD', 'timestamp': 1491008502, 'credit': 0, 'channel_type': 'matchbook',
             'side': 'lay', 'size': 60.0, 'runner_id': 450147584080010, 'runner': 'Utah Jazz', 'price': 1.66},
            {'market_id': '450147584000010', 'order_type': 'GFD', 'timestamp': 1491008502, 'credit': 0, 'channel_type': 'matchbook',
             'side': 'back', 'size': 40.0, 'runner_id': 450147584030010, 'runner': 'Washington Wizards', 'price': 2.48},
            {'market_id': '450147584000010', 'order_type': 'GFD', 'timestamp': 1491008502, 'credit': 0, 'channel_type': 'matchbook',
             'side': 'lay', 'size': 7.0, 'runner_id': 450147584030010, 'runner': 'Washington Wizards', 'price': 2.22}
        ]

        orders_transposed = dict(zip(order_list[0], zip(*[d.values() for d in order_list])))

        resp = self.api.betting.send_orders(
            runner_id=list(orders_transposed.get('runner_id', ())),
            odds=list(orders_transposed.get('price', ())),
            side=list(orders_transposed.get('side', ())),
            stake=list(orders_transposed.get('size', ())),
            temp_id=orders_transposed.get('customer_reference'),
        )
