from DontEdit import *
import datetime


dateTime = open("YearToYear.txt", "a")

try:
    def year():
        old_year = int(input("Input the year you want to know how long ago was: "))
        current_year = datetime.datetime.now().year
        YearsAgo = current_year - old_year
        if old_year == current_year:
            print(f"{BRIGHT}{RED}[-]{RESET} The year you put in is today. Plase input a diffrent year")
            return year()
        elif old_year > current_year:
            print(f"{BRIGHT}{RED}[-]{RESET} That year doesn't exist yet. Plase input a diffrent year")
        else:
            if YearsAgo == int(1):
                print(f"\nThe year '{old_year}' was '{YearsAgo}' year ago.")
                print(f"\nThe year '{old_year}' was '{YearsAgo}' year ago.",file=dateTime)

            elif YearsAgo > int(1):
                print(f"\nThe year '{old_year}' was '{YearsAgo}' years ago.")
                print(f"\nThe year '{old_year}' was '{YearsAgo}' years ago.",file=dateTime)

    year()
except KeyboardInterrupt:
    print(f'\nKeyboardInterrupt')