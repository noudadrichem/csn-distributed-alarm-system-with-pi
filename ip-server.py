import socket 

maartenIP = '192.168.42.2'
port = 6677 
buffer = 1024
message = 'hello maarten from noud'

server = socket.socket()
print('socket created')
server.bind((maartenIP, port))
server.listen(4)
print('socket listening on 4')
client_socket, client_address = server.accept()
print(client_address, "has connected")

while True:
    c, addr = server.accept()
    print('got connection from ', addr)
    c.send('True'.encode())

    c.close()
