from typing import Tuple, Union


supported_schemas = ('http://', 'https://', 'file://')


def includesSchema(url: str) -> bool:
    return len(url.split('//', 1)) > 1


def throwOnInvalidSchema(url: str):
    """ Throws error if URL does not start with http schema """
    if includesSchema(url):
        assert url.startswith(supported_schemas)


def getSchema(url: str) -> str:
    return url.split('//', 1)[0] + '//' if includesSchema(url) else ''


def stripSchema(url: str) -> str:
    """ Strips supported schema (http) from provided url """
    throwOnInvalidSchema(url)
    return url[len(getSchema(url)):]


def extractHostAndPath(urlWithoutSchema: str) -> Tuple[str, str]:
    """ Returns the host and path from the provided schemaless url """
    return urlWithoutSchema.split('/', 1)


def extractPortFromHost(host: str) -> Union[int, None]:
    """ If found, returns the port read from the host string """
    if ':' in host:
        port = host.split(':', 1)[1]
        return int(port)

    return None
