import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.38', 9999))
server.listen()

client, addr = server.accept()

file_name = client.reciv(1024).decode()
print(file_name)
file_size = client.accept(10245).decode()
print(file_size)

file = open(file_name, 'wb')

file_bytes = b""

done = False

proggress = tqdm.tqdm(unit='B', unit_scale=True, unit_divisor=1000, total=int(file_size))

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data
        proggress.update(len(data))