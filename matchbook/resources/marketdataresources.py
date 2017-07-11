from matchbook.resources import BaseResource


class Price(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'prices'
        attributes = {
            'available-amount': 'available-amount',
            'currency': 'currency',
            'decimal-odds': 'decimal-odds',
            'exchange-type': 'exchange-type',
            'odds': 'odds',
            'odds-type': 'odds-type',
            'side': 'side',
        }


class Runner(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'runners'
        attributes = {
            'event-id': 'event-id',
            'event-participant-id': 'event-participant-id',
            'id': 'id',
            'market-id': 'market-id',
            'name': 'name',
            'status': 'status',
            'volume': 'volume',
            'withdrawn': 'withdrawn',
        }
        sub_resources = {
            'prices': Price,
        }


class Market(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'markets'
        attributes = {
            'allow-live-betting': 'allow-live-betting',
            'back-overround': 'back-overround',
            'event-id': 'event-id',
            'grading-type': 'grading-type',
            'handicap': 'handicap',
            'id': 'id',
            'in-running-flag': 'in-running-flag',
            'lay-overround': 'lay-overround',
            'market-ids': 'market-ids',
            'name': 'name',
            'runner-ids': 'runner-ids',
            'start': 'start',
            'status': 'status',
            'type': 'type',
            'market-type': 'market-type',
            'volume': 'volume',
        }
        sub_resources = {
            'runners': Runner,
        }
        datetime_attributes = (
            'start'
        )


class EventMeta(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'meta-tags'
        attributes = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'url-name': 'url-name',
        }


class Event(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'allow-live-betting': 'allow-live-betting',
            'category-id': 'category-id',
            'id': 'id',
            'in-running-flag': 'in-running-flag',
            'name': 'name',
            'sport-id': 'sport-id',
            'start': 'start',
            'status': 'status',
            'volume': 'volume',
        }
        sub_resources = {
            'markets': Market,
            'meta-tags': EventMeta,
        }
        datetime_attributes = (
            'start'
        )
