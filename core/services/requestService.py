from sys import path
from core.services.schemaService import SchemaService
from typing import Dict, Tuple, Union
from xml.sax import parseString
from utils.url import captureHostFromUrl, is_relative_path
from utils.string import camelCaseToKebabCase
from utils.requestHelper import RequestHelper
from core.constants.constants import MAX_REDIRECT_COUNT, RESPONSE_NEW_LINE, HttpHeaders
import socket
from utils.responseHelper import ResponseHelper


class RequestService:
    def __init__(self, socket: socket.socket, protocol: str = 'https'):
        self.socket = socket
        self.protocol = protocol.upper()

    def request(self, *, path: str, count=0, **headers) -> Tuple[Dict, str]:
        targetPath = f'GET {path}.html HTTP/1.0\r\n'
        targetHeaders = ''.join([RequestHelper.createHeader(
            camelCaseToKebabCase(key), value) + RESPONSE_NEW_LINE for key, value in headers.items()])
        end = RESPONSE_NEW_LINE

        try:
            self.socket.send((targetPath +
                              targetHeaders + end).encode('utf8'))
        except Exception as error:
            print('Error sending from socket: ', error)

        response = self.socket.makefile(
            'r', encoding='utf8', newline=RESPONSE_NEW_LINE)

        parsed_response = ResponseHelper.parseResponse(response)
        if self.__is_redirect(parsed_response) and count < MAX_REDIRECT_COUNT:
            print('Redirecting to...  ',
                  parsed_response[1][HttpHeaders.LOCATION.value])
            return self.request(self.__get_path_from_location_header(parsed_response[1][HttpHeaders.LOCATION.value]), **headers)

        return parsed_response

    def __is_redirect(self, response: Tuple[int, Dict, str]) -> bool:
        status, headers, _ = response

        return status >= 300 and status < 400 and headers[HttpHeaders.LOCATION.value]

    def __get_path_from_location_header(self, location: str) -> str:
        if is_relative_path(location):
            base_url = captureHostFromUrl(path)
            return f'{base_url}{location}'

        return location
