from utils.responseHelper import ResponseHelper
from core.socket import create_socket
from utils.url import extractHostAndPath

print(extractHostAndPath('browser.engineering/http.html'))

socket = create_socket()
socket.connect(('example.org', 80))

bytes_send = socket.send(b"GET /index.html HTTP/1.0\r\n" +
                         b"Host: example.org\r\n\r\n")

print('Bytes send {}', bytes_send)

response = socket.makefile('r', encoding='utf8', newline='\r\n')

headers, body = ResponseHelper.parseResponse(response)

print('Headers: {}'.format(headers))
print('Body: {}'.format(body))

socket.close()
