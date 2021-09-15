from enum import Enum

RESPONSE_NEW_LINE = '\r\n'


class Ports(Enum):
    HTTP = 80
    HTTPS = 443


class Schema(Enum):
    SOURCE = 'view-source:'
    HTML = 'data:text/html'
    FILE = 'file://'
    HTTP = 'http://'
    HTTPS = 'https://'
