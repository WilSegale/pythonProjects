from datetime import datetime, timedelta

def get_current_time():
    return datetime.now().time()

def add_time(clock_time, hours, minutes):
    time_obj = datetime.strptime(clock_time, "%I:%M %p")  # Use %I for 12-hour format
    time_delta = timedelta(hours=hours, minutes=minutes)
    new_time = (time_obj + time_delta).strftime('%I:%M %p')  # Use %I for 12-hour format
    return new_time

def subtract_time(clock_time, hours, minutes):
    time_obj = datetime.strptime(clock_time, "%I:%M %p")  # Use %I for 12-hour format
    time_delta = timedelta(hours=hours, minutes=minutes)
    new_time = (time_obj - time_delta).strftime('%I:%M %p')  # Use %I for 12-hour format
    return new_time

def main():
    try:
        while True:
            print("Clock Calculator")
            print("1. Get current time")
            print("2. Add time")
            print("3. Subtract time")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                current_time = get_current_time()
                print(f"\nCurrent time: {current_time.strftime('%I:%M %p')}\n")  # Use %I for 12-hour format
            elif choice == "2":
                clock_time = input("Enter the current time (hh:mm AM/PM): ")
                hours = int(input("Enter the number of hours to add: "))
                minutes = int(input("Enter the number of minutes to add: "))
                new_time = add_time(clock_time, hours, minutes)
                print(f"New time: {new_time}")
            elif choice == "3":
                clock_time = input("Enter the current time (hh:mm AM/PM): ")
                hours = int(input("Enter the number of hours to subtract: "))
                minutes = int(input("Enter the number of minutes to subtract: "))
                new_time = subtract_time(clock_time, hours, minutes)
                print(f"New time: {new_time}")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please select a valid option.")
    except KeyboardInterrupt:
        print("\n[-]exitting program")
if __name__ == "__main__":
    main()
