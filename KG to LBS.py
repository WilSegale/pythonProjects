# Function to convert kilograms to pounds
def kg_to_lbs(kg):
    lbs = kg * 2.20462
    return lbs

# Example usage
kg = float(input("Input the KG you want to covert to LBS: "))
lbs = kg_to_lbs(kg)
print(f"{kg:,.2f} kilograms is equal to {lbs:,.2f} pounds")
