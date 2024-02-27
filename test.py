import os
import socket
print("hello world")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
file = open("test.txt", "rb")
file_size = os.path.getsize("test.txt")

client.send("revicedFile.txt".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()
