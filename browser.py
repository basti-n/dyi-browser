from core.services.htmlDisplayService import HTMLDisplayService
from core.services.socketService import SocketService
from utils.url import extractHostAndPath
from core.services.requestService import RequestService

print(extractHostAndPath('browser.engineering/http.html'))


def start(host: str = 'example.org') -> None:
    socket_service = SocketService(host)
    socket = socket_service.create()
    socket_service.connect()

    request_service = RequestService(socket)
    headers, body = request_service.request(
        path='/index', host=host, connection='close', userAgent="custom")

    htmlService = HTMLDisplayService(body)
    htmlService.show()

    socket.close()


if __name__ == '__main__':
    import sys
    start(sys.argv[1])
