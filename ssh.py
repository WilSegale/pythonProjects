import os

username = input("Input the UserName: ")
hostname = input("Input the hostname or IP Address: ")

os.system(f"ssh {username}@{hostname}")