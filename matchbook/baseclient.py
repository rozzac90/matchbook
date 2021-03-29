import requests
import os

from matchbook.exceptions import PasswordError
from matchbook.enums import ExchangeType, OddsType, Currency


class BaseClient(object):

    def __init__(self, username=None, password=None, locale=None):
        """
        :param username: Matchbook username.
        :param password: Password for supplied username, if None will look in for MATCHBOOK_PW in env variables.
        """
        self.username = username
        self.password = password
        self.locale = locale
        self.url = 'https://www.matchbook.com'
        self.url_beta = 'https://beta.matchbook.com'
        self.urn_main = '/bpapi/rest/'
        self.urn_edge = '/edge/rest/'
        self.session = requests.Session()
        self.session_token = None
        self.user_id = None
        self.exchange_type = ExchangeType.BackLay
        self.odds_type = OddsType.Decimal
        self.currency = Currency.EUR
        self.get_username()
        self.get_password()

    def set_session_token(self, session_token, user_id):
        """Sets session token.
        
        :param session_token: Session token from request.
        :param user_id: User Id from the request.
        """
        self.session_token = session_token
        self.user_id = user_id

    def get_password(self):
        """If password is not provided will look in environment
        variables for username+'password'
        """
        if self.password is None:
            if os.environ.get('MATCHBOOK_PW'):
                self.password = os.environ.get('MATCHBOOK_PW')
            else:
                raise PasswordError()

    def get_username(self):
        """If password is not provided will look in environment
        variables for username+'password'
        """
        if self.username is None:
            if os.environ.get('MATCHBOOK_USER'):
                self.username = os.environ.get('MATCHBOOK_USER')
            else:
                raise PasswordError()


    @property
    def headers(self):
        """Set headers to be used in API requests."""
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
