
import json

if not hasattr(json, 'JSONDecodeError'):
    json.JSONDecodeError = ValueError
else:
    from json.decoder import JSONDecodeError


class MBError(Exception):
    pass


class NotLoggedIn(MBError):
    pass


class AuthError(MBError):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        try:
            self.message = response.json().get('errors')[0].get('messages')
        except:
            self.message = 'UNKNOWN'
        super(AuthError, self).__init__(self.message)


class ApiError(MBError):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        try:
            error_data = response.json().get('errors')
            self.message = error_data[0].get('messages', 'UNKNOWN')

        except (KeyError, JSONDecodeError, TypeError):
            self.message = 'UNKNOWN'
            print(response)
        super(ApiError, self).__init__(self.message)


class PasswordError(MBError):
    """Exception raised if password is not found"""

    def __init__(self):
        message = 'Password not found in environment variables, add or pass to APIClient'
        super(PasswordError, self).__init__(message)


class StatusCodeError(MBError):

    def __init__(self, status_code):
        message = 'Status code error: %s' % status_code
        super(StatusCodeError, self).__init__(message)

