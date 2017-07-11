from matchbook.resources.baseresource import BaseResource


class SportsDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
        }


class OddsType(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'odds-type': 'odds-type',
            'odds-type-id': 'odds-type-id',
        }


class Currencies(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'currency-id': 'currency-id',
            'long-name': 'long-name',
            'short-name': 'short-name',
        }


class Countries(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'country-id': 'country-id',
            'name': 'name',
            'country-code': 'country-code',
        }


class Regions(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'region-id': 'region-id',
            'name': 'name',
        }


class MetaTags(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {

        }
