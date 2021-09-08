from typing import Tuple, Union


supported_schema = 'http://'


def throwOnInvalidSchema(url: str):
    """ Throws error if URL does not start with http schema """
    assert url.startswith(supported_schema)


def stripSchema(url: str) -> str:
    """ Strips supported schema (http) from provided url """
    throwOnInvalidSchema(url)
    return url[len(supported_schema):]


def extractHostAndPath(urlWithoutSchema: str) -> Tuple[str, str]:
    """ Returns the host and path from the provided schemaless url """
    return urlWithoutSchema.split('/', 1)


def extractPortFromHost(host: str) -> Union[int, None]:
    """ If found, returns the port read from the host string """
    if ':' in host:
        port = host.split(':', 1)[1]
        return int(port)

    return None
