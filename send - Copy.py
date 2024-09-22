import os
import socket

print("hello world")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

file_name = "test.txt"
file_size = os.path.getsize(file_name)

# Send file name and size
client.sendall(f"{file_name},{file_size}".encode())

# Open the file and send its content in chunks
with open(file_name, "rb") as file:
    while True:
        chunk = file.read(1024)  # Read 1KB at a time
        if not chunk:
            break  # End of file
        client.sendall(chunk)

# Signal the end of file transmission
client.send(b"<END>")

client.close()
