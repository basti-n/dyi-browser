from core.constants.constants import Schema
from core.services.schemaService import SchemaService
from core.services.htmlDisplayService import HTMLDisplayService
from core.services.socketService import SocketService
from utils.url import extractHostAndPath
from core.services.requestService import RequestService
from core.services.fileService import FileService

print(extractHostAndPath('browser.engineering/http.html'))


def start(host: str = 'example.org') -> None:
    schemaService = SchemaService(host)

    if schemaService.schema == Schema.FILE.value:
        fileService = FileService()
        fileService.readFile(schemaService.schemalessPath)
        return

    if not schemaService.schema or schemaService.schema == Schema.HTTP.value or schemaService.schema == Schema.HTTPS.value:
        socket_service = SocketService(host)
        socket = socket_service.create()
        socket_service.connect()

        request_service = RequestService(socket)
        headers, body = request_service.request(
            path='/index', host=host, connection='close', userAgent="custom")

        htmlService = HTMLDisplayService(body)
        htmlService.show()

        socket.close()
        return


if __name__ == '__main__':
    import sys
    start(sys.argv[1])
