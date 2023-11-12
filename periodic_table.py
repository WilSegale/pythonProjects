# Import necessary modules
from DontEdit import *
from elements import *
from htmlfile import *
import csv

# Open or create a JSON file for appending (note: it's generally better to open it in 'w' mode for writing)
JSON_FILE = open("element.json", "a")

# Function to retrieve an element by atomic number
def AtomicNumber():
    try:
        while True:
            # Input an atomic number or 'exit' to quit
            ChosenElement = input("Input an atomic number (1-118) to select an element (or type 'exit' to quit): ")
            if ChosenElement.lower() == 'exit':
                break

            ChosenElement = int(ChosenElement)

            if 1 <= ChosenElement <= 118:
                # Find the element with the specified atomic number
                element = next((el for el in elements if el["atomic_number"] == ChosenElement), None)
                if element:
                    # Display element details
                    print(f'\nName: {element["name"]} [{element["symbol"]}]', end=" ")
                    print(f'Atomic Number: {element["atomic_number"]}', end=" ")
                    print(f'Atomic Weight: {element["atomic_weight"]}\n')

                    # Create a list for CSV output
                    AtomicNumber = [
                        ['CHOOSEN FUNCTION', 'AtomicNumber'],
                        ['Name', element["name"]],
                        ['Symbol', element["symbol"]],
                        ['Atomic Number', element["atomic_number"]],
                        ['Weight', element["atomic_weight"]]
                    ]

                    # Write CSV data to a file
                    csv_file_path = 'AtomicNumber.csv'
                    with open(csv_file_path, 'w', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerows(AtomicNumber)

                    # Generate an HTML file for the selected element
                    html_output = generate_element_html(element)  # Make sure you have the 'generate_element_html' function implemented.
                    with open(f"element_{element['atomic_number']}.html", "w") as html_file:
                        html_file.write(html_output)
                    print(f"HTML file 'element_{element['atomic_number']}.html' has been generated.")
                else:
                    print("Element not found.")
            else:
                print(f"{BRIGHT}{ORANGE_Start}[*]{ORANGE_END} Invalid Atomic Number.")
    except KeyboardInterrupt:
        print(f"\n{BRIGHT}{RED}[-]{RESET} Keyboard Interrupt")

# Function to retrieve an element by name
def AtomicName():
    try:
        while True:
            # Input an element name or 'exit' to quit
            ChosenElement = input("Input an element name to select an element (or type 'exit' to quit): ")
            if ChosenElement.lower() == 'exit':
                break

            chosen_element = None
            for element in elements:
                # Find the element with the specified name (case-insensitive)
                if element["name"].lower() == ChosenElement.lower():
                    chosen_element = element
                    break

            if chosen_element:
                # Display element details
                print(f'\nName: {chosen_element["name"]} [{element["symbol"]}]', end=" ")
                print(f'Atomic Number: {chosen_element["atomic_number"]}', end=" ")
                print(f'Atomic Weight: {chosen_element["atomic_weight"]}\n')

                # Create a list for CSV output
                AtomicName = [
                    ['CHOOSEN FUNCTION', 'AtomicName'],
                    ['Name', element["name"]],
                    ['Symbol', element["symbol"]],
                    ['Atomic Number', element["atomic_number"]],
                    ['Weight', element["atomic_weight"]]
                ]

                # Write CSV data to a file
                csv_file_path = 'AtomicName.csv'
                with open(csv_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(AtomicName)

                # Generate an HTML file for the selected element
                html_output = generate_element_html(chosen_element)  # Make sure you have the 'generate_element_html' function implemented.
                with open(f"element_{chosen_element['atomic_number']}.html", "w") as html_file:
                    html_file.write(html_output)
                print(f"HTML file 'element_{chosen_element['atomic_number']}.html' has been generated.")
            else:
                print(f'{BRIGHT}{ORANGE_Start}[*]{ORANGE_END} Atomic Name not found ')
    except KeyboardInterrupt:
        print(f"\n{BRIGHT}{RED}[-]{RESET} Keyboard Interrupt")

# Function to retrieve an element by symbol
def symbol():
    try:
        while True:
            # Input a symbol or 'exit' to quit
            ChosenElement = input("Input a symbol to select an element (or type 'exit' to quit): ")
            if ChosenElement.lower() == 'exit':
                break

            chosen_element = None
            for element in elements:
                # Find the element with the specified symbol (case-insensitive)
                if element["symbol"].lower() == ChosenElement.lower():
                    chosen_element = element
                    break

            if chosen_element:
                # Display element details
                print(f'\nName: {chosen_element["name"]} [{element["symbol"]}]', end=" ")
                print(f'Atomic Number: {chosen_element["atomic_number"]}', end=" ")
                print(f'Atomic Weight: {chosen_element["atomic_weight"]}\n')

                # Create a list for CSV output
                symbol = [
                    ['CHOOSEN FUNCTION', 'SYMBOL'],
                    ['Name', element["name"]],
                    ['Symbol', element["symbol"]],
                    ['Atomic Number', element["atomic_number"]],
                    ['Weight', element["atomic_weight"]]
                ]

                # Write CSV data to a file
                csv_file_path = 'symbol.csv'
                with open(csv_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(symbol)

                # Generate an HTML file for the selected element
                html_output = generate_element_html(chosen_element)  # Make sure you have the 'generate_element_html' function implemented.
                with open(f"element_{chosen_element['atomic_number']}.html", "w") as html_file:
                    html_file.write(html_output)
                print(f"HTML file 'element_{chosen_element['atomic_number']}.html' has been generated.")
            else:
                print(f'{BRIGHT}{ORANGE_Start}[*]{ORANGE_END} Symbol not found')
    except KeyboardInterrupt:
        print(f"\n{BRIGHT}{RED}[*]{RESET} Keyboard Interrupt")

# Input a number from 1-118 to select an element
choices = float(input("Do you want to see the atomic number(1), or element name(2). Or symbol (3): "))

if choices == 1:
    AtomicNumber()
elif choices == 2:
    AtomicName()
elif choices == 3:
    symbol()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
    exit(1)
