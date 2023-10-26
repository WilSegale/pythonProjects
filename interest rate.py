
# Define the initial amount and final amount
initial_amount = int(input("input the initial amount: "))
final_amount = int(input("input the final amount: "))

# Calculate the interest rate
interest_rate = ((final_amount - initial_amount) / initial_amount) * 100

# Print the result
print(f"The interest rate is {interest_rate}%")
