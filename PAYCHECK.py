import datetime

# Date of the last paycheck
last_paycheck = datetime.date(2023, 4, 28)

# Pay frequency in days
pay_frequency = 14

# Calculate the next paycheck date
next_paycheck = last_paycheck + datetime.timedelta(days=pay_frequency)

# Print the date of the next paycheck
print(f"Your next paycheck is on: {next_paycheck}")
