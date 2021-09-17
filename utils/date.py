from datetime import datetime
from time import time


def httpDateToUnixTime(httpDatetime: str) -> int:
    """ For the passed date string returns the no of ms passed since Epoch time """
    format = '%a, %d %b %Y %H:%M:%S GMT'
    try:
        return int(datetime.strptime(httpDatetime, format).timestamp())
    except Exception as error:
        print('Error converting {} to Unix Time. Error Message: {}'.format(
            httpDatetime, error))


def getCurrentUnixTime() -> int:
    """ Returns the current unix time as integer """
    return int(time())
