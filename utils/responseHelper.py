from core.constants.constants import RESPONSE_NEW_LINE
from typing import Dict, TextIO, Tuple


class ResponseHelper:

    @staticmethod
    def parseResponse(response: TextIO) -> Tuple[Dict, str]:
        status_line = response.readline()
        version, status, explaination = status_line.split(' ', 2)
        assert status == '200', '{}: {}'.format(status, explaination)

        headers = ResponseHelper.extractHeaders(response)
        body = response.read()

        return (headers, body)

    @staticmethod
    def extractHeaders(response: TextIO) -> Dict:
        headers = {}
        while True:
            line = response.readline()
            if line == RESPONSE_NEW_LINE:
                break

            header, value = line.split(':', 1)
            headers[header.lower()] = value.strip()

        return headers
