import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and port to listen on
receiver_ip = '192.168.1.38'  # Replace with the receiver's IP address
receiver_port = 22  # Replace with the same port as in the sender

# Bind the socket to the IP address and port
s.bind((receiver_ip, receiver_port))

# Listen for incoming connections
s.listen()

print(f"Listening on {receiver_ip}:{receiver_port}...")

# Accept the connection
conn, addr = s.accept()
print(f"Connection from {addr}")

# Receive and print the data
data = conn.recv(1024).decode()
print(f"Received: {data}")

# Close the connection and the socket
conn.close()
s.close()
