from DontEdit import  *
try:
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
        
        tasks_done = 0
        for ip in ip_list:
            for port in port_range:
                tasks_done += 1
                if scan_port(str(ip), port):
                    print(f"[ {GREEN}+{RESET} ] {ip}:{port} is open ")
                    open_ports.append(f"{ip}:{port}")
                
                # Calculate and print ETA
                elapsed_time = time.time() - start_time
                avg_time_per_task = elapsed_time / tasks_done
                tasks_left = total_tasks - tasks_done
                eta = avg_time_per_task * tasks_left

                print(f"Progress: {tasks_done}/{total_tasks}, ETA: {time.strftime('%H:%M:%S', time.gmtime(eta))}", end='\r')
        
        return open_ports

    # Get user input to store in a JSON file
    def save_message_to_txt(data):
        file_path = 'output.txt'
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)  # indent for pretty-printing
        except IOError as e:
            print(f"Error saving to file: {e}")

    # Define the network range and port range
    print("Enter the network range (e.g., 192.168.1.0/24):")
    network = input(">>> ")  # Store the network range as a string

    # Function to parse the port range input (e.g., 20-1024)
    def parse_port_range(port_range_str):
        try:
            start, end = map(int, port_range_str.split('-'))
            return list(range(start, end + 1))
        except ValueError:
            print("Invalid port range format. Please enter a valid range (e.g., 20-1024).")
            return []

    # Get and parse port range input
    port_range_input = input("Enter the port range (e.g., 20-1024):\n>>> ")

    port_range = parse_port_range(port_range_input)
    if port_range_input == "*" or port_range_input == "all":
        port_range = list(range(1, 65536))

    if not port_range:
        print("Invalid port range. Exiting.")
    else:
        # Run the network scanner
        if __name__ == "__main__":
            open_ports = network_scan_with_eta(network, port_range)

            # Sample data (text) to write to a JSON file
            data = {
                "open_ports": open_ports
            }
            
            # If there are open ports, store them along with the user's message
            if open_ports:

                # Save the user's message and open ports to a JSON file
                save_message_to_txt(data)
            else:
                print(f"[ {RED}-{RESET} ] No open ports found.")
except KeyboardInterrupt:
    print(f"\n[ {RED}-{RESET} ] Exiting")