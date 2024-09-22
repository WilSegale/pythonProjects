# created on 
# Date: 2023-21-10
# Time: 4:29 PM

# Function to convert megatons to tons
def megatons_to_tons(megatons):
    return megatons * 1000000

# Function to convert pounds to tons
def pounds_to_tons(pounds):
    return pounds / 2000

# Function to ask if the user wants to calculate the number of megatons or pounds in a ton
def main():
    try:
        choice = int(input("Enter (1) to calculate the number of megatons in a ton. Or (2) for the amout of pounds in a ton: "))
        
        if choice == 1:
            megatons()
        
        elif choice == 2:
            pounds()
        
        else:
            print("Invalid input. Please enter 1 or 2.")
            return main()
    
    except KeyboardInterrupt:
        print("\nProgram terminated...")
        exit(1)

# megaton calculation to Ton
def megatons():
    try:
        # Example usage:
        megatons = float(input("Enter the number of megatons: "))  # Read input as a float
        tons = megatons_to_tons(megatons)

        # Format output as a string
        output_str = f"{megatons} megatons is equal to {tons:,.2f} tons"

        # HTML output with proper structure
        html_output = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>MegaTon to Ton or LBS to TON Calculation Result</title>
            <style>
                #MegaTon {{
                    color: red;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h1>MegaTon to TON Calculation Result</h1>
            <p>Number of MegaTon is a result of Tons:</p>
            <p id="MegaTon">{output_str}</p>
        </body>
        </html>
        """

        # Write the HTML string to an HTML file in 'write' mode
        with open('MegaTon.html', 'a') as html_file:
            html_file.write(html_output)

        print(f"{megatons} megatons is equal to {tons:,.2f} tons")
    except KeyboardInterrupt:
        print("\nProgram terminated...")
        exit(1)

# LBS calculation to Ton
def pounds():
    try:
        # Example usage:
        pounds = float(input("Enter the number of pounds: "))
        tons = pounds_to_tons(pounds)

        # Format output as a string
        output_str = f"{pounds} LBS is equal to {tons:,.2f} tons"

        # HTML output with proper structure
        html_output = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>MegaTon to Ton or LBS to TON Calculation Result</title>
            <style>
                #LBS {{
                    color: red;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h1>LBS to TON Calculation Result</h1>
            <p>Number of LBS is a result of Tons:</p>
            <p id="LBS">{output_str}</p>
        </body>
        </html>
        """

        # Write the HTML string to an HTML file in 'write' mode
        with open('MegaTon.html', 'a') as html_file:
            html_file.write(html_output)

        print(f"{pounds} LBS is equal to {tons:,.2f} tons")
    except KeyboardInterrupt:
        print("\nProgram terminated...")
        exit(1)

if __name__ == "__main__":
    main()