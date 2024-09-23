import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

client, addr = server.accept()

# Receive file name and size
file_info = client.recv(1024).decode().split(',')
file_name = file_info[0]
file_size = int(file_info[1])

print(file_name)
print(file_size)

file = open(file_name, 'wb')

progress = tqdm.tqdm(unit='B', unit_scale=True, unit_divisor=1000, total=file_size)

while True:
    data = client.recv(1024)
    if not data:
        break
    file.write(data)
    progress.update(len(data))

file.close()
client.close()
server.close()
