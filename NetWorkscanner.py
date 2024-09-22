import socket
import ipaddress
import json

# Function to scan a specific port on an IP address
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Set timeout for the connection
        result = sock.connect_ex((ip, port))  # Try to connect to the port
        sock.close()
        if result == 0:  # Port is open if result is 0
            return True
        else:
            return False
    except socket.error:
        return False

# Function to scan a range of IP addresses and ports
def network_scan(network, port_range):
    open_ports = []
    print(f"Scanning network {network} on ports {port_range}")
    for ip in ipaddress.IPv4Network(network, strict=False):
        for port in port_range:
            if scan_port(str(ip), port):
                print(f"[+] {ip}:{port} is open")
                open_ports.append(f"{ip}:{port}")
    return open_ports

# Get user input to store in a JSON file
def save_message_to_json():
    # Prompt the user to enter a message

   

    # Specify the file path where you want to save the JSON file
    file_path = 'output.json'

    # Writing data to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # indent for pretty-printing

# Define the network range and port range
network = '127.0.0.1'  # Replace with your network range (e.g., 192.168.1.0/24)
port_range = range(20, 50)  # Ports to scan (20-1024)

# Run the network scanner
if __name__ == "__main__":
    open_ports = network_scan(network, port_range)
     # Sample data (text) to write to a JSON file
    data = {
        "message": open_ports,
        "author": "WilSegale"
    }
    # If there are open ports, store them along with the user's message
    if open_ports:
        print(f"\nOpen Ports found: {open_ports}")

        # Save the user's message and open ports to a JSON file
        save_message_to_json()
    else:
        print("No open ports found.")
