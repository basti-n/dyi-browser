from core.constants.constants import RESPONSE_NEW_LINE, Schema
from core.services.schemaService import SchemaService
from core.services.htmlDisplayService import HTMLDisplayService
from core.services.socketService import SocketService
from utils.url import extractDataFromHost
from core.services.requestService import RequestService
from core.services.fileService import FileService


def start(host: str = 'example.org') -> None:
    schemaService = SchemaService(host)

    if schemaService.schema == Schema.FILE.value:
        fileService = FileService()
        fileService.readFile(schemaService.schemalessPath)
        return

    if schemaService.schema == Schema.HTML.value:
        html = extractDataFromHost(host)
        htmlService = HTMLDisplayService(html)
        htmlService.show()
        return

    if not schemaService.schema or schemaService.schema == Schema.HTTP.value or schemaService.schema == Schema.HTTPS.value or schemaService.schema == Schema.SOURCE.value:
        is_view_source = schemaService.schema == Schema.SOURCE.value

        socket_service = SocketService(
            schemaService.schemalessPath if is_view_source else host)
        socket = socket_service.create(secure=True)
        socket_service.connect()

        request_service = RequestService(socket)
        status, headers, body = request_service.request(
            path='/index', host=schemaService.host, connection='close', userAgent="custom", acceptEncoding="gzip, deflate, br")

        htmlService = HTMLDisplayService(body)
        htmlService.show(view_source=is_view_source)

        betweenBodyTag = htmlService.findAllBetweenTag(body, 'body')
        print(htmlService.show(body=RESPONSE_NEW_LINE.join(betweenBodyTag)))

        socket.close()
        return


if __name__ == '__main__':
    import sys
    start(sys.argv[1])
