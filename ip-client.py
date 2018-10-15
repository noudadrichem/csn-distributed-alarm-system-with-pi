import socket

HOST = '192.168.42.1'
PORT = 6677

s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello PINOUD')
data = s.recv(1024)

print('recieved', repr(data))


