import socket 

server = socket.socket()
port = 6677
server.connect(('127.0.0.1', port))


server.send('This is a string from client')


valueFromServer = (server.recv(1024))

if eval(valueFromServer):
    print('De value vanuit de server is True')
else:
    print('de value vanuit de server is False')

'''
while True:
    client, addr = server.accept()
    recvieved_data = client_socket.recv(1024)
    print(recvieved_data)
'''
server.close()
input()
