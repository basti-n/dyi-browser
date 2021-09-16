from typing import Tuple, Union
from urllib.parse import urlparse


supported_schemas = ('http://', 'https://', 'file://',
                     'data:text/html', 'view-source:')


def hasRegularSchema(url: str) -> bool:
    return len(url.split('//', 1)) > 1


def hasDataSchema(url: str) -> bool:
    return 'data' in url


def hasViewSourceSchema(url: str) -> bool:
    return 'view-source' in url


def includesSchema(url: str) -> bool:
    return hasRegularSchema(url) or hasDataSchema(url) or hasViewSourceSchema(url)


def throwOnInvalidSchema(url: str):
    """ Throws error if URL does not start with http schema """
    if includesSchema(url):
        assert url.startswith(supported_schemas)


def is_relative_path(url: str) -> bool:
    """ Returns true for relative paths (starting with '/') """
    return url.startswith('/')


def getSchema(url: str) -> str:
    if hasRegularSchema(url):
        return url.split('//', 1)[0] + '//'
    if hasDataSchema(url):
        return url.split(',', 1)[0]
    if hasViewSourceSchema(url):
        return url.split(':', 1)[0] + ':'

    return ''


def stripSchema(url: str) -> str:
    """ Strips supported schema (e.g. http, https) from provided url """
    throwOnInvalidSchema(url)
    return url[len(getSchema(url)):]


def extractHostAndPath(urlWithoutSchema: str) -> Tuple[str, str]:
    """ Returns the host and path from the provided schemaless url """
    return urlWithoutSchema.split('/', 1)


def extractAfter(input: str, predicate: str) -> Union[int, None]:
    """ Returns the matched input after the predicate (if found) """
    if predicate in input:
        match = input.split(predicate, 1)[1]
        return match

    return None


def extractPortFromHost(host: str) -> Union[int, None]:
    """ If found, returns the port read from the host string """
    port = extractAfter(host, ':')
    return int(port) if port else None


def extractDataFromHost(host: str) -> Union[int, None]:
    """ Returns the data from the passed data url host """
    return extractAfter(host, ',')


def extractUrlFromViewSource(host: str) -> Union[str, None]:
    """ If found, returns the url part of the provided view source uri """
    return extractAfter(host, ':')


def captureHostFromUrl(url: str) -> str:
    """ Returns the network location of the provided url """
    return urlparse(url).netloc
