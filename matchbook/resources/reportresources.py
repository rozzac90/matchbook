from matchbook.resources.baseresource import BaseResource


class BetReport(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'event-id': 'event-id',
            'event-name': 'event-name',
            'exchange-type': 'exchange-type',
            'market-id': 'market-id',
            'market-type': 'market-type',
            'odds': 'odds',
            'offer-id': 'offer-id',
            'profit-and-loss': 'profit-and-loss',
            'runner-id': 'runner-id',
            'selection': 'selection',
            'side': 'side',
            'sport-id': 'sport-id',
            'stake': 'stake',
            'submitted-at': 'submitted-at',
        }
        datetime_attributes = (
            'submitted-at'
        )


class SettlementBet(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'bets'
        attributes = {
            'profit-and-loss': 'profit-and-loss',
            'matched-time': 'matched-time',
            'odds': 'odds',
            'commission-rate': 'commission-rate',
            'in-play': 'in-play',
            'offer-id': 'offer-id',
            'id': 'id',
            'settled-time': 'settled-time',
            'stake': 'stake',
            'commission': 'commission'
        }


class SettlementSelection(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'selections'
        attributes = {
            'name': 'name',
            'odds': 'odds',
            'profit-and-loss': 'profit-and-loss',
            'id': 'id',
            'side': 'side',
            'stake': 'stake',
            'commission': 'commission'
        }
        sub_resources = {
            'bets': SettlementBet
        }


class SettlementMarket(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'markets'
        attributes = {
            'profit-and-loss': 'profit-and-loss',
            'net-win-commission': 'net-win-commission',
            'name': 'name',
            'id': 'id',
            'commission': 'commission',
            'stake': 'stake',
        }
        sub_resources = {
            'selections': SettlementSelection
        }


class SettlementEvent(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'events'
        attributes = {
            'sport-url': 'sport-url',
            'start-time': 'start-time',
            'sport-name': 'sport-name',
            'name': 'name',
            'id': 'id',
            'sport-id': 'sport-id',
            'finished-dead-heat': 'finished-dead-heat'
        }
        sub_resources = {
            'markets': SettlementMarket
        }


class SettlementReport(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'offset': 'offset',
            'profit-and-loss': 'profit-and-loss',
            'odds-type': 'odds-type',
            'total': 'total',
            'per-page': 'per-page',
            'language': 'language',
            'overall-staked-amount': 'overall-staked-amount'
        }
        sub_resources = {
            'events': SettlementEvent
        }
        datetime_attributes = (
            'settled-at'
        )


class MarketSettlementReport(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'exchange-type': 'exchange-type',
            'odds': 'odds',
            'profit-and-loss': 'profit-and-loss',
            'runner-id': 'runner-id',
            'runner-name': 'runner-name',
            'side': 'side',
            'stake': 'stake',
            'settled-at': 'settled-at',
        }
        datetime_attributes = (
            'settled-at'
        )


class RunnerSettlementReport(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'bet-id': 'bet-id',
            'exchange-type': 'exchange-type',
            'market-id': 'market-id',
            'odds': 'odds',
            'offer-id': 'offer-id',
            'offer-type': 'offer-type',
            'placed-at': 'placed-at',
            'profit-and-loss': 'profit-and-loss',
            'runner-id': 'runner-id',
            'runner-name': 'runner-name',
            'settled-at': 'settled-at',
            'side': 'side',
            'stake': 'stake',
            'trade-type': 'trade-type',
        }
        datetime_attributes = (
            'settled-at',
            'placed-at'
        )


class CommissionReport(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'commission': 'commission',
            'commissionable-handle': 'commissionable-handle',
            'offer-type': 'offer-type',
            'placed-at': 'placed-at',
            'rate': 'rate',
            'runner-id': 'runner-id',
            'runner-name': 'runner-name',
            'settled-at': 'settled-at',
            'trade-type': 'trade-type',
        }
        datetime_attributes = (
            'settled-at',
            'placed-at'
        )


class TransactionReport(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'balance': 'balance',
            'category': 'category',
            'debit': 'debit',
            'detail': 'detail',
            'time-settled': 'time-settled',
            'type': 'type',
        }
        datetime_attributes = (
            'time-settled'
        )