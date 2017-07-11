import json

from matchbook.utils import check_status_code, check_call_complete


class BaseEndpoint(object):

    def __init__(self, parent):
        """
        :param parent: API client.
        """
        self.client = parent

    def request(self, request_method, urn, method, params={}, data={}, target=None, session=None):
        """
        :param request_method: type of request to be sent.
        :param urn: matchbook urn to append to url specified.
        :param method: Matchbook method to be used.
        :param params: Params to be used in request.
        :param data: data to be sent in request body.
        :param target: target to get from returned data, if none returns full response.
        :param session: Requests session to be used, reduces latency.
        """
        session = session or self.client.session
        data['session-token'] = self.client.session_token
        data['user-id'] = self.client.user_id
        request_url = '%s%s%s' % (self.client.url, urn, method)
        response = session.request(
            request_method, request_url, params=params, data=json.dumps(data), headers=self.client.headers
        )
        check_status_code(response)
        if ('per-page' in params.keys()) and target:
            resp_data = response.json().get(target, [])
            while not check_call_complete(response.json()):
                params['offset'] += response.json().get('total', 0) + 1
                response = session.request(
                    request_method, request_url, params=params, data=json.dumps(data), headers=self.client.headers
                )
                resp_data += response.json().get(target, [])
            return resp_data
        else:
            return response

    @staticmethod
    def process_response(response_json, resource, date_time_sent, date_time_received=None):
        """
        :param response_json: Response in json format
        :param resource: Resource data structure
        :param date_time_sent: Date time sent
        :param date_time_received: Date time received response from request
        """
        if isinstance(response_json, list):
            return [
                resource(date_time_sent=date_time_sent, TIMESTAMP=date_time_received.strftime('%Y-%m-%d %H:%M:%S.%f'),
                         **x).json() for x in response_json]
        else:
            response_result = response_json.get('result', response_json)
            if isinstance(response_result, list):
                return [resource(date_time_sent=date_time_sent,
                                 TIMESTAMP=date_time_received.strftime('%Y-%m-%d %H:%M:%S.%f'),
                                 **x).json() for x in response_result]
            else:
                return resource(date_time_sent=date_time_sent,
                                TIMESTAMP=date_time_received.strftime('%Y-%m-%d %H:%M:%S.%f'),
                                **response_result).json()
