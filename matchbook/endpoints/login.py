
from matchbook.endpoints.baseendpoint import BaseEndpoint
from matchbook.exceptions import AuthError


class Login(BaseEndpoint):

    def __call__(self, session=None):
        response = self.request("POST", self.client.urn_main, 'security/session', data=self.data, session=session)
        response_json = response.json()
        self.client.set_session_token(response_json.get('session-token'), response_json.get('user-id'))

    @property
    def data(self):
        return {'username': self.client.username, 'password': self.client.password}

