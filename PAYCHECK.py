from DontEdit import *
import datetime

# Set the date of your last paycheck
last_paycheck_date = datetime.date(2023, 4, 11)  # Change this to your last paycheck date

# Calculate the next Friday
days_until_friday = (4 - last_paycheck_date.weekday()) % 7
next_friday = last_paycheck_date + datetime.timedelta(days_until_friday)

# Calculate the next bi-weekly Friday
days_until_next_paycheck = 14
while next_friday < last_paycheck_date + datetime.timedelta(days_until_next_paycheck):
    next_friday += datetime.timedelta(days=7)

# Print the date of the next paycheck
print(GREEN+"Your next paycheck is on", next_friday.strftime("%A, %B %d, %Y")+RESET)
