import socket

sock = socket.socket()
sock.connect(('localhost', 8000))
sock.send((b'hello, world!'))
data = sock.recv(1024)
sock.close()
