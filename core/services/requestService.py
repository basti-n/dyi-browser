from core.constants.constants import RESPONSE_NEW_LINE
import socket
from utils.responseHelper import ResponseHelper


class RequestService:
    def __init__(self, socket: socket.socket):
        self.socket = socket

    def request(self, *, path: str, host: str) -> None:
        targetPath = f'GET {path}.html HTTP/1.0\r\n'.encode('utf8')
        targetHost = f'Host: {host}\r\n\r\n'.encode('utf8')

        self.socket.send(targetPath +
                         targetHost)

        response = self.socket.makefile(
            'r', encoding='utf8', newline=RESPONSE_NEW_LINE)

        return ResponseHelper.parseResponse(response)
