import socket

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()
    except:
        print("Error during scan")

host = input("Enter host to scan: ")

for port in range(1, 65535):
    port_scanner(host, port)
