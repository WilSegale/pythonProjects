print("Input the amount of hours to covert to days")
hours = input(">>> ")

print(hours, "hours is", float(hours) / 24, "days")
if float(hours) / 24 > 1:
    print(f"That is {float(hours) / 24} days")
else:
    print(f"That is {float(hours) / 24} day")
