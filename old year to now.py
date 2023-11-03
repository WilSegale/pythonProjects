import datetime


dateTime = open("YearToYear.txt", "a")

try:
    def year():
        old_year = int(input("Input the year you want to know how long ago was: "))
        current_year = datetime.datetime.now().year
        if old_year == current_year:
            print("The year you put in is today. Plase input a diffrent year")
            return year()
        else:
            print(f"The year '{old_year}' was '{current_year - old_year}' years ago.")
            print(f"The year '{old_year}' was '{current_year - old_year}' years ago.",file=dateTime)
    year()
except KeyboardInterrupt:
    print(f'\nKeyboardInterrupt')