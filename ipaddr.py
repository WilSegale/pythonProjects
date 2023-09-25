# Prints the IP of the host
from DontEdit import *
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(IP)