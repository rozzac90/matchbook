from matchbook.resources.baseresource import BaseResource


class MatchedBets(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'matched-bets'
        attributes = {
            'commission': 'commission',
            'created-at': 'created-at',
            'currency': 'currency',
            'decimal-odds': 'decimal-odds',
            'id': 'id',
            'odds': 'odds',
            'odds-type': 'odds-type',
            'potential-profit': 'potential-profit',
            'stake': 'stake',
        }
        datetime_attributes = (
            'created-at'
        )


class Order(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'created-at': 'created-at',
            'currency': 'currency',
            'decimal-odds': 'decimal-odds',
            'event-id': 'event-id',
            'event-name': 'event-name',
            'exchange-type': 'exchange-type',
            'id': 'id',
            'market-id': 'market-id',
            'market-name': 'market-name',
            'odds': 'odds',
            'odds-type': 'odds-type',
            'potential-profit': 'potential-profit',
            'remaining': 'remaining',
            'remaining-potential-profit': 'remaining-potential-profit',
            'runner-id': 'runner-id',
            'runner-name': 'runner-name',
            'side': 'side',
            'stake': 'stake',
            'status': 'status',
        }
        sub_resources = {
            'matched-bets': MatchedBets,
        }
        datetime_attributes = (
            'created-at'
        )


class Position(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {

        }