import os


def start():
   os.system("dir");
   CHOICE = input("Enter your choice: ");
   print(f"{CHOICE} is selected");
   if CHOICE == "python.executable":
      print('eror')
   os.system(f"{CHOICE}");
start()