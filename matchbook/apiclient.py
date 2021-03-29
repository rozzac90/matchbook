from matchbook.baseclient import BaseClient
from matchbook import endpoints


class APIClient(BaseClient):

    def __init__(self, username=None, password=None):
        super(APIClient, self).__init__(username, password)

        self.login = endpoints.Login(self)
        self.keep_alive = endpoints.KeepAlive(self)
        self.logout = endpoints.Logout(self)
        self.betting = endpoints.Betting(self)
        self.account = endpoints.Account(self)
        self.market_data = endpoints.MarketData(self)
        self.reference_data = endpoints.ReferenceData(self)
        self.reporting = endpoints.Reporting(self)

    def __repr__(self):
        return '<APIClient [%s]>' % self.username

    def __str__(self):
        return 'APIClient'
