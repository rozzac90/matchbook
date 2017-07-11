from matchbook.endpoints.baseendpoint import BaseEndpoint
from matchbook.exceptions import AuthError
from matchbook.utils import logger


class Logout(BaseEndpoint):

    def __call__(self, session=None):
        response = self.request("DELETE", self.client.urn_main, 'security/session', data=self.data, session=session)
        self.client.set_session_token(None, None)
        logger.info('Logout Successful. Session Token: {}'.format(self.client.session_token))

    @property
    def data(self):
        return {'username': self.client.username, 'password': self.client.password}
