from enum import Enum

RESPONSE_NEW_LINE = '\r\n'
MAX_REDIRECT_COUNT = 3


class Ports(Enum):
    HTTP = 80
    HTTPS = 443


class Schema(Enum):
    SOURCE = 'view-source:'
    HTML = 'data:text/html'
    FILE = 'file://'
    HTTP = 'http://'
    HTTPS = 'https://'


class HttpHeaders(Enum):
    CACHE_CONTROL = 'cache-control'
    LOCATION = 'location'
    DATE = 'date'


class CacheControlHeaders(Enum):
    REVALIDATE = 'must-revalidate'
    NO_CACHE = 'no-cache'
    NO_SOTRE = 'no-store'
