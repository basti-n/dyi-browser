from core.socket import create_socket
from utils.url import extractHostAndPath

print(extractHostAndPath('browser.engineering/http.html'))

socket = create_socket()
