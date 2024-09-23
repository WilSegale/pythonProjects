import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the server details
host = ''  # Leave empty to accept connections on all available network interfaces
port = 12345  # Choose a suitable port number

# Bind the socket to the server address
s.bind((host, port))

# Listen for incoming connections
s.listen(1)

# Accept a connection from the sender
print("Waiting for a connection...")
connection, address = s.accept()
print("Connected!")

# Receive data
data = connection.recv(1024)
print("Received:", data.decode())

# Close the connection and socket
connection.close()
s.close()
