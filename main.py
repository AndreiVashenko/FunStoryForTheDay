import socket
import requests


r = requests.post('https://api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/sendMessage?chat_id=6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg&text=Privet')

statusCod = r.status_code;


#_command = b'http://api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/getUpdates'

#_command = 'GET /bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/getUpdates #HTTP/1.1\r\nHost:api.telegram.org\r\n\r\n'.encode()

_command = 'GET  https://api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/getUpdates HTTP/1.1\r\n\r\n'.encode()

#_command = 'GET /api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/sendMessage?chat_id=6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg&text=Privet HTTP/1.1\r\nHost:api.telegram.org\r\n\r\n'.encode()

HOST = 'api.telegram.org'  # The remote host
PORT = 443 # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(_command)
  data = s.recv(1024)
  if data:
    #pass
    print('Received:\n\r', repr(data))


