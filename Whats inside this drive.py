import os

os.system("ls -l /Volumes")
Drive = input("Drive: ")
external_drive_path = f"/Volumes/{Drive}"  # Replace with the correct name of your external drive
os.chdir(external_drive_path)

contents = os.listdir()
print(contents)
