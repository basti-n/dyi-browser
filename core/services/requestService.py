from typing import Union
from utils.string import camelCaseToKebabCase
from utils.requestHelper import RequestHelper
from core.constants.constants import RESPONSE_NEW_LINE
import socket
from utils.responseHelper import ResponseHelper


class RequestService:
    def __init__(self, socket: socket.socket, protocol: str = 'https'):
        self.socket = socket
        self.protocol = protocol.upper()

    def request(self, *, path: str, **headers) -> None:
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

        return ResponseHelper.parseResponse(response)
