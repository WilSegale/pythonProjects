from DontEdit import json
from elements import *
from htmlfile import *

file_name = "elements.json"
with open(file_name, "w") as json_file:
    json.dump(elements, json_file, indent=4)

# Corrected function name
def AtomicNumber():
    try:
        while True:
            ChosenElement = input("Input an atomic number (1-118) to select an element (or type 'exit' to quit): ")
            if ChosenElement.lower() == 'exit':
                break

            ChosenElement = int(ChosenElement)

            if 1 <= ChosenElement <= 118:
                element = next((el for el in elements if el["atomic_number"] == ChosenElement), None)
                if element:
                    print(f'\nName: {element["name"]} [{element["symbol"]}]', end=" ")
                    print(f'Atomic Number: {element["atomic_number"]}', end=" ")
                    print(f'Atomic Weight: {element["atomic_weight"]}\n')

                    # Generate an HTML file for the selected element
                    html_output = generate_element_html(element)  # Make sure you have the 'generate_element_html' function implemented.
                    with open(f"element_{element['atomic_number']}.html", "w") as html_file:
                        html_file.write(html_output)
                    print(f"HTML file 'element_{element['atomic_number']}.html' has been generated.")
                else:
                    print("Element not found.")
            else:
                print("Invalid atomic number.")
    except KeyboardInterrupt:
        print("\n[-] Keyboard Interrupt")

def AtomicName():
    try:
        while True:
            ChosenElement = input("Input an element name to select an element (or type 'exit' to quit): ")
            if ChosenElement.lower() == 'exit':
                break

            chosen_element = None
            for element in elements:
                if element["name"].lower() == ChosenElement.lower():
                    chosen_element = element
                    break

            if chosen_element:
                print(f'\nName: {chosen_element["name"]} [{element["symbol"]}]', end=" ")
                print(f'Atomic Number: {chosen_element["atomic_number"]}', end=" ")
                print(f'Atomic Weight: {chosen_element["atomic_weight"]}\n')

                # Generate an HTML file for the selected element
                html_output = generate_element_html(chosen_element)  # Make sure you have the 'generate_element_html' function implemented.
                with open(f"element_{chosen_element['atomic_number']}.html", "w") as html_file:
                    html_file.write(html_output)
                print(f"HTML file 'element_{chosen_element['atomic_number']}.html' has been generated.")
    
    except KeyboardInterrupt:
        print("\n[-] Keyboard Interrupt")

# Write the data to the JSON file

print(f"Data has been written to {file_name}.")

# Input a number from 1-118 to select an element
choices = int(input("Do you want to see the atomic number(1). Or element name(2): "))

if choices == 1:
    AtomicNumber()

elif choices == 2:
    AtomicName()
    
else:
    print("Invalid choice. Please enter 1 or 2.")
