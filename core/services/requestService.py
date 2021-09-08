from typing import Union
from core.constants.constants import RESPONSE_NEW_LINE
import socket
from utils.responseHelper import ResponseHelper


class RequestService:
    def __init__(self, socket: socket.socket, protocol: str = 'https'):
        self.socket = socket
        self.protocol = protocol.upper()

    def request(self, *, path: str, host: str) -> None:
        targetPath = f'GET {path}.html HTTP/1.0\r\n'
        targetHost = f'Host: {host}\r\n\r\n'

        try:
            self.socket.send((targetPath +
                              targetHost).encode('utf8'))
        except Exception as error:
            print('Error sending from socket: ', error)

        response = self.socket.makefile(
            'r', encoding='utf8', newline=RESPONSE_NEW_LINE)

        return ResponseHelper.parseResponse(response)
