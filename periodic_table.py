from elements import *
import json

# Remove the unused index 0
elements.pop(0)

# Write the data to the JSON file
file_name = "elements.json"
with open(file_name, "w") as json_file:
    json.dump(elements, json_file, indent=4)

print(f"Data has been written to {file_name}.")

# Input a number from 1-118 to select an element
ChosenElement = input("Input an atomic number (1-118) to select an element: ")

try:
    ChosenElement = int(ChosenElement)
    if 1 <= ChosenElement <= 118:
        element = next((el for el in elements if el["atomic_number"] == ChosenElement), None)
        if element:
            print(element)
        else:
            print("Element not found.")
    else:
        print("Invalid atomic number.")
        
except ValueError:
    print("Invalid input. Please enter a valid atomic number.")