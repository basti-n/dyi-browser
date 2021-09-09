from enum import Enum

RESPONSE_NEW_LINE = '\r\n'


class Ports(Enum):
    HTTP = 80
    HTTPS = 443


class Schema(Enum):
    FILE = 'file://'
    HTTP = 'http://'
    HTTPS = 'https://'
