from DontEdit import *
import datetime

with open("YearToYear.txt", "w") as dateTime:
    def year():
        try:
            old_year = int(input("Input the year you want to know how long ago was: "))
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            return year()

        current_year = datetime.datetime.now().year
        YearsAgo = current_year - old_year

        if old_year == current_year:
            print(f"{BRIGHT}{RED}[-]{RESET} The year you put in is today. Please input a different year")
        elif old_year > current_year:
            print("That year doesn't exist yet. Please input a different year")
        else:
            if YearsAgo == 1:
                print(f"\nThe year '{old_year}' was '{YearsAgo}' year ago.")
            elif YearsAgo > 1:
                print(f"\nThe year '{old_year}' was '{YearsAgo}' years ago.")
            else:
                print(f"\nThe year '{old_year}' was '{YearsAgo}' years ago.", file=dateTime)

    while True:
        try:
            year()
            break  # Exit the loop if the year function is executed without exceptions
        except KeyboardInterrupt:
            print(f'\nKeyboardInterrupt')
