from core.socket import create_socket
import socket


class SocketService():

    def create(self) -> socket.socket:
        self.socket = create_socket()
        return self.socket

    def connect(self, host: str) -> None:
        if not self.socket:
            print('No Socket found. Please create socket first.')

        else:
            self.socket.connect((host, 80))
