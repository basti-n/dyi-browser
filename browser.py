from core.socket import create_socket
from utils.url import extractHostAndPath
from core.services.requestService import RequestService

print(extractHostAndPath('browser.engineering/http.html'))

socket = create_socket()
socket.connect(('example.org', 80))

request_service = RequestService(socket)
headers, body = request_service.request(path='/index', host='example.org')

print('Headers: {}'.format(headers))
print('Body: {}'.format(body))

socket.close()
