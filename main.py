import socket
import requests

#mess = requests.get('https://api.telegram.org:443/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/sendMessage?#&chat_id=6044383569&text=Privet')

#mess = requests.get('https://api.telegram.org:443/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/getUpdates')

#if not mess:
#  print('error')

#statusCod = r.status_code;

#_command = b'GET #https://api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/sendMessage?#&chat_id=6044383569&text=Privet HTTP/1.1'

_command = b'GET https://api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/getUpdates'



HOST = 'api.telegram.org'  # The remote host
PORT = 443  # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(_command)
  data = s.recv(1024)
  if data:
    #pass
    print('Received:\n\r', repr(data))
