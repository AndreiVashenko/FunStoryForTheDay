import socket

HOST = 'api.telegram.org'  # The remote host
PORT = 80  # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(
      "https://api.telegram.org/bot6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg/название_метода"
  )
  data = s.recv(1024)
print('Received', repr(data))
