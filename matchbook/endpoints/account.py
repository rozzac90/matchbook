import datetime

from matchbook.endpoints.baseendpoint import BaseEndpoint
from matchbook import resources
from matchbook.utils import clean_locals


class Account(BaseEndpoint):

    def get_account(self, balance_only=True, session=None):
        """
        Get account information for logged in user.

        :param balance_only: retrieve only account balance info subset or not.
        :type balance_only: bool
        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Returns the account details for the logged-in user.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError

        """
        method = 'account'
        resource = resources.AccountDetails
        if balance_only:
            method = 'account/balance'
            resource = resources.AccountBalance
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_edge, method, session=session)
        date_time_received = datetime.datetime.utcnow()
        return self.process_response(response.json(), resource, date_time_sent, date_time_received)

    def wallet_transfer(self, amount, session=None):
        #TODO: Populate Acccount Transfer Resource.
        """
        Transfer balance from one 
        
        :param amount: amount to be transferred, >0 for casino to sports transfer, <0 for the opposite.
        :type amount: float
        :param session: requests session to be used.
        :type session: requests.Session
        :return: details of the success/failure of the transfer.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        date_time_received = datetime.datetime.utcnow()
        response = self.request("POST", self.client.urn_main, 'account/transfer', data=params, session=session)
        return self.process_response(response.json(), resources.AccountTransfer, date_time_sent, date_time_received)

    def get_casino_balance(self, session=None):
        """
        Get casino account balance for logged in user.

        :param session: requests session to be used.
        :type session: requests.Session
        :returns: Returns the casino balance for the logged-in user.
        :rtype: json
        :raises: MatchbookAPI.bin.exceptions.ApiError

        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request("GET", self.client.urn_main, 'account/balance', session=session)
        date_time_received = datetime.datetime.utcnow()
        return self.process_response(response.json(), resources.AccountBalance, date_time_sent, date_time_received)
