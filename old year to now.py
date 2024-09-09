# Importing necessary modules
from DontEdit import *
import datetime

# Opening a file for writing date and time information
dateTime = open("YearToYear.txt", "a")

try:
    # Function to calculate the number of years ago a given year is
    def year():
        # Taking user input for the year
        old_year = int(input("Input the year you want to know how long ago was: "))
        
        # Getting the current year
        current_year = datetime.datetime.now().year
        
        # Calculating the years ago
        YearsAgo = current_year - old_year

        # Handling different cases
        if old_year == current_year:
            print(f"{BRIGHT}{RED}[-]{RESET} The year you put in is today. Please input a different year")
            return year()
        elif old_year > current_year:
            print(f"{BRIGHT}{RED}[-]{RESET} That year doesn't exist yet. Please input a different year")
        else:
            # Printing and writing the result to the file
            if YearsAgo == int(1):
                print(f"\nThe year '{old_year}' was '{YearsAgo}' year ago.")
                print(f"\nThe year '{old_year}' was '{YearsAgo}' year ago.", file=dateTime)
            elif YearsAgo > int(1):
                print(f"\nThe year '{old_year}' was '{YearsAgo}' years ago.")
                print(f"\nThe year '{old_year}' was '{YearsAgo}' years ago.", file=dateTime)

    # Calling the year function
    year()

except KeyboardInterrupt:
    print(f'\nKeyboardInterrupt')
