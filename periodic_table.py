from DontEdit import *
from elements import elements
from htmlfile import *
import json




# Write the data to the JSON file
file_name = "elements.json"
with open(file_name, "w") as json_file:
    json.dump(elements, json_file, indent=4)

print(f"Data has been written to {file_name}.")

# Input a number from 1-118 to select an element
try:
    while True:
        ChosenElement = input("Input an atomic number (1-118) to select an element (or type 'exit' to quit): ")

        if ChosenElement.lower() == 'exit':
            break

        ChosenElement = int(ChosenElement)
        if 1 <= ChosenElement <= 118:
            # Try to find the selected element by atomic number
            element = next((el for el in elements if el["atomic_number"] == ChosenElement), None)
            if element:
                print(f'\nName: {element["name"]} [{element["symbol"]}]', end=" ")
                print(f'Atomic Number: {element["atomic_number"]}', end=" ")
                print(f'Atomic Weight: {element["atomic_weight"]}\n')

                # Generate an HTML file for the selected element
                html_output = generate_element_html(element)
                with open(f"element_{element['atomic_number']}.html", "w") as html_file:
                    html_file.write(html_output)
                print(f"HTML file 'element_{element['atomic_number']}.html' has been generated.")
            else:
                print("Element not found.")
        else:
            print("Invalid atomic number.")

except ValueError:
    print("Invalid input. Please enter a valid atomic number.")

except KeyboardInterrupt:
    print("\nInterrupted by the user.")
