import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = int(client.recv(1024).decode())  # Receive file size as an integer
print(file_size)

file = open(file_name, 'wb')

proggress = tqdm.tqdm(unit='B', unit_scale=True, unit_divisor=1000, total=file_size)

while True:
    data = client.recv(1024)
    if not data:
        break
    file.write(data)
    proggress.update(len(data))

file.close()
client.close()
server.close()
