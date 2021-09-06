import socket
from core.erroLogger import log_error


def create_socket() -> socket.socket:
    try:
        s = socket.socket(family=socket.AF_INET,
                          proto=socket.IPPROTO_TCP, type=socket.SOCK_STREAM)

    except:
        log_error('Failed creating socket.')

    return s
