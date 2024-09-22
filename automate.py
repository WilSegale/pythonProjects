import socket


def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to any remote server, it doesn't matter which one
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
        # Get the IP address associated with the socket
    except Exception as e:
        print("Error:", e)
        ip_address = None
    finally:
        # Close the socket
        s.close()

    return ip_address

# Call the function to get the IP address
ip_address = get_ip_address()
print(f"Your IP address is: {ip_address}")