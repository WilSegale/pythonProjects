import os
import subprocess

if os.path.exists("D:\\"):
    print('Externial hard drive is connected')
    eject = input("Would you link to eject the hard drive: ")
    if eject == "yes":
        subprocess.run(['eject',"D:"])
    else:
        print("Ok Drive will not be ejected")
else:
    print("No externial hard drvie is connected to this computer")