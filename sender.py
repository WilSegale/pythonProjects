import socket

s = socket.socket()
host = s.gethostname()
port = 8080
s.bind((host,port))

s.listen(1)
print("waiting for connection")
