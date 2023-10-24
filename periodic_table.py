from elements import *
from DontEdit import *
import json

# Define the list of elements (You should define the elements list here)

# Write the data to the JSON file
file_name = "elements.json"
with open(file_name, "w") as json_file:
    json.dump(elements, json_file, indent=4)

print(f"Data has been written to {file_name}.")

# Input a number from 1-118 to select an element
try:
    while True:
        ChosenElement = input("Input an atomic number (1-118) to select an element (or type 'exit' to quit): ")
        if ChosenElement == "exit":
            print("\nInterrupted by the user.")
            break
        ChosenElement = int(ChosenElement)
        if 1 <= ChosenElement <= 118:
            # Try to find the selected element by atomic number
            element = next((el for el in elements if el["atomic_number"] == ChosenElement), None)
            if element:
                print(f"\n{GREEN}{element}{RESET}")
            else:
                print("Element not found.")
        else:
            print("Invalid atomic number.")
            
except ValueError:
    print("Invalid input. Please enter a valid atomic number.")
    
except KeyboardInterrupt:
    print("\nInterrupted by the user.")
