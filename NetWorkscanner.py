import socket
import ipaddress
import json
import time

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

# Function to scan a range of IP addresses and ports with ETA
def network_scan_with_eta(network, port_range):
    open_ports = []
    ip_list = list(ipaddress.IPv4Network(network, strict=False))
    total_ips = len(ip_list)
    total_ports = len(port_range)
    total_tasks = total_ips * total_ports
    start_time = time.time()

    print(f"Scanning network {network} on ports {port_range}")
    
    tasks_done = 0
    for ip in ip_list:
        for port in port_range:
            tasks_done += 1
            if scan_port(str(ip), port):
                print(f"[+] {ip}:{port} is open")
                open_ports.append(f"{ip}:{port}")
            
            # Calculate and print ETA
            elapsed_time = time.time() - start_time
            avg_time_per_task = elapsed_time / tasks_done
            tasks_left = total_tasks - tasks_done
            eta = avg_time_per_task * tasks_left

            print(f"Progress: {tasks_done}/{total_tasks}, ETA: {time.strftime('%H:%M:%S', time.gmtime(eta))}", end='\r')
    
    return open_ports

# Get user input to store in a JSON file
def save_message_to_json(data):
    # Specify the file path where you want to save the JSON file
    file_path = 'output.json'

    # Writing data to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # indent for pretty-printing

# Define the network range and port range
network = '127.0.0.1'  # Replace with your network range (e.g., 192.168.1.0/24)
port_range = range(0, 22)  # Ports to scan (20-1024)

# Run the network scanner
if __name__ == "__main__":
    open_ports = network_scan_with_eta(network, port_range)

    # Sample data (text) to write to a JSON file
    data = {
        "message": open_ports,
        "author": "WilSegale"
    }
    
    # If there are open ports, store them along with the user's message
    if open_ports:
        print(f"\nOpen Ports found: {open_ports}")

        # Save the user's message and open ports to a JSON file
        save_message_to_json(data)
    else:
        print("No open ports found.")
