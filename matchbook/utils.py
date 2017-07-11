
import sys
import datetime
import logging
from matchbook.exceptions import ApiError

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
    format=LOG_FORMAT,
)

logger = logging.getLogger(__name__)


def clean_time(col):
    """
    Parse a UTC time column to datetime.

    :param col: column to be parsed.
    :returns: datetime column
    :rtype: series

    """
    return col.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))


def filter_dicts(d):
    """
    Filter dict to remove None values.

    :param d: data to filter
    :type d: dict
    :returns: filtered data
    :rtype: dict

    """
    return dict((k, v) for k, v in d.items() if v is not None)


def clean_locals(params):
    """
    Clean up locals dict, remove empty and self params.

    :params params: locals dicts from a function.
    :type params: dict
    :returns: cleaned locals dict to use as params for functions
    :rtype: dict
    """
    clean_params = dict((k, v) for k, v in params.items() if v is not None and k != 'self' and k != 'session')
    for k, v in clean_params.items():
        if '_' in k:
            new_key = k.replace('_', '-')
            clean_params[new_key] = v
            clean_params.pop(k)
    return clean_params


def check_call_complete(response):
    return response.get('total', 0) < response.get('per-page', 20)


def check_status_code(response, codes=None):
    """Checks response.status_code is in codes
    :param response: Requests response
    :param codes: List of accepted codes or callable
    :raises: StatusCodeError if code invalid
    """
    codes = codes or [200]
    if response.status_code not in codes:
        raise ApiError(response)
