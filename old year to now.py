import datetime

try:
    def year():
        old_year = int(input("Input the year you want to know how long ago was: "))
        current_year = datetime.datetime.now().year
        print(f"The year '{old_year}' was '{current_year - old_year}' years ago.")
    year()
except KeyboardInterrupt:
    print(f'\nerror: KeyboardInterrupt')