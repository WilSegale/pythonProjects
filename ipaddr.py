import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(IP)