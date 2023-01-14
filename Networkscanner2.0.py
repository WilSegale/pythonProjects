import concurrent.futures
import socket

def scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"[+] Port {port} is open on {host}")
    else:
        print(f"[-] Port {port} is closed on {host}")
    sock.close()

def main():
    host_list = ["host1", "host2", "host3"]
    port = 80
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(scan, host, port) for host in host_list]
        for f in concurrent.futures.as_completed(results):
            pass
        print(port)

if __name__ == "__main__":
    main()
