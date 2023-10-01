# Define the initial amount and final amount
initial_amount = int(input(">>> "))
final_amount = int(input(">>> "))

# Calculate the interest rate
interest_rate = ((final_amount - initial_amount) / initial_amount) * 100

# Print the result
print(f"The interest rate is {interest_rate}%")
