import socket


sock = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)
sock.bind(('localhost', 8000))
sock.listen(1)
while True:
    connection, client_address = sock.accept()
    data = connection.recv(1024)
    if data:
        connection.sendall(data.upper())
    else:
        connection.close()