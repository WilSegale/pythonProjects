import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the connection details
host = '192.168.1.13'  # IP address of the receiving computer
port = 12345  # Choose a suitable port number

# Connect to the receiver
s.connect((host, port))

# Send data
data = b'Hello, receiver!'
s.send(data)

# Close the socket
s.close()