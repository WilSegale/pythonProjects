from DontEdit import *
from elements import *
from htmlfile import *


JSON_FILE = open("element.json", "a")

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
                print(f"{BRIGHT}{RED}[*]{RESET} Invalid Atomic Number.")
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
            else:
                print(f'{BRIGHT}{RED}[*]{RESET} Atomic Name not found ')
    except KeyboardInterrupt:
        print("\n[-] Keyboard Interrupt")

def symbol():
    try:
        while True:
            ChosenElement = input("Input an symbol to select an element (or type 'exit' to quit): ")
            if ChosenElement.lower() == 'exit':
                break

            chosen_element = None
            for element in elements:
                if element["symbol"].lower() == ChosenElement.lower():
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
            else:
                print(f'{BRIGHT}{RED}[*]{RESET} Symbol not found')
    except KeyboardInterrupt:
        print(f"\n{BRIGHT}{RED}[*]{RESET} Keyboard Interrupt")

# Input a number from 1-118 to select an element
choices = int(input("Do you want to see the atomic number(1), or element name(2). Or symbol (3): "))

if choices == 1:
    AtomicNumber()

elif choices == 2:
    AtomicName()

elif choices == 3:
    symbol()

else:
    print("Invalid choice. Please enter 1, 2 or 3.")