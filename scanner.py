import socket
try:
    def scan_port(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            return True
        except:
            return False

    def scan_host(host):
        for port in range(1, 65535):
            if scan_port(host, port):
                print(f"{host}:{port} is open")

    def scan_network(network):
        for i in range(1, 255):
            host = f"{network}.{i}"
            scan_host(host)

    if __name__ == "__main__":
        network = "192.168.1.1"
        scan_network(network)
except KeyboardInterrupt:
    print("\nExiting....")