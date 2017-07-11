from matchbook.resources.baseresource import BaseResource


class AccountDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'balance': 'balance',
            'bet-slip-pinned': 'bet-slip-pinned',
            'commission-reserve': 'commission-reserve',
            'commission-type': 'commission-type',
            'currency': 'currency',
            'email': 'email',
            'exchange-type': 'exchange-type',
            'exposure': 'exposure',
            'family-names': 'family-names',
            'free-funds': 'free-funds',
            'given-names': 'given-names',
            'language': 'language',
            'odds-type': 'odds-type',
            'roles': 'roles',
            'show-bet-confirmation': 'show-bet-confirmation',
            'show-odds-rounding-message': 'show-odds-rounding-message',
            'show-position': 'show-position',
            'status': 'status',
            'user-id': 'user-id',
            'username': 'username'
        }


class AccountBalance(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'balance': 'balance',
            'commission-reserve': 'commission-reserve',
            'exposure': 'exposure',
            'free-funds': 'free-funds',
        }


class AccountTransfer(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {

        }
