import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and port of the receiver
receiver_ip = '192.168.1.100'  # Replace with the receiver's IP address
receiver_port = 22  # Replace with the receiver's port

# Connect to the receiver
s.connect((receiver_ip, receiver_port))

# Data to be sent
message = "Hello, receiver!"

# Send the data
s.sendall(message.encode())

# Close the socket
s.close()
