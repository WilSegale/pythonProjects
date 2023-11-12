from DontEdit import *
import datetime


dateTime = open("YearToYear.txt", "a")

try:
    def year():
        old_year = int(input("Input the year you want to know how long ago was: "))
        current_year = datetime.datetime.now().year
        if old_year == current_year:
            print(f"{BRIGHT}{RED}[-]{RESET} The year you put in is today. Plase input a diffrent year")
            return year()
        elif old_year > current_year:
            print("That year doesn't exist yet. Plase input a diffrent year")
        else:
            print(f"The year '{old_year}' was '{current_year - old_year}' years ago.")
            print(f"The year '{old_year}' was '{current_year - old_year}' years ago.",file=dateTime)
    year()
except KeyboardInterrupt:
    print(f'\nKeyboardInterrupt')