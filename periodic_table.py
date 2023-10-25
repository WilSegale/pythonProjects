from DontEdit import *
from elements import elements
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

        ChosenElement = int(ChosenElement)
        if 1 <= ChosenElement <= 118:
            # Try to find the selected element by atomic number
            element = next((el for el in elements if el["atomic_number"] == ChosenElement), None)
            if element:
                print(f'''\nName: {element['name']}{GREEN}[{element['symbol']}]{RESET}''',
                      f'''atomic_number{GREEN}[{element["atomic_number"]}]{RESET}''',
                      f'''atomic_weight{GREEN}[{element["atomic_weight"]}]{RESET}\n''')
                # Generate an HTML file for the selected element
                html_output = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Element Details</title>
                </head>
                <body>
                    <h1>Name: {element['name']} ({element['symbol']})</h1>
                    <p>Atomic Number: {element['atomic_number']}</p>
                    <p>Atomic Weight: {element['atomic_weight']}</p>
                </body>
                </html>
                """
                with open("element_details.html", "w") as html_file:
                    html_file.write(html_output)
                print("HTML file 'element_details.html' has been generated.")
            else:
                print("Element not found.")
        else:
            print("Invalid atomic number.")
            
except ValueError:
    print("Invalid input. Please enter a valid atomic number.")
    
except KeyboardInterrupt:
    print("\nInterrupted by the user.")
