# Import the 'escape' function from the 'html' module
from html import escape

# Function to calculate the number of chest X-rays needed
def calculate_xray_count(exposure_roentgen, exposure_per_xray_mR):
    try:
        # Convert user input to floating-point numbers
        exposure_roentgen = float(exposure_roentgen)
        exposure_per_xray_mR = float(exposure_per_xray_mR)
        
        # Convert exposure in roentgens to milliroentgens
        exposure_mR = exposure_roentgen * 1000
        
        # Calculate the number of chest X-rays needed
        xray_count = exposure_mR / exposure_per_xray_mR
        
        return xray_count
    
    except ValueError:
        return "Invalid input. Please enter valid numeric values."

# Main program
if __name__ == "__main__":
    # Prompt the user to enter the desired exposure in roentgens (R)
    exposure_roentgen = input("Enter the desired exposure in roentgens (R): ")
    
    # Prompt the user to enter the exposure per chest X-ray in milliroentgens (mR)
    exposure_per_xray_mR = input("Enter the exposure per chest X-ray in milliroentgens (mR): ")

    # Call the 'calculate_xray_count' function to calculate the result
    result = calculate_xray_count(exposure_roentgen, exposure_per_xray_mR)
    
    # Format the result as a floating-point number with 2 decimal places
    formatted_result = '{:,.2f}'.format(result)

    # Format the user's input values similarly
    formatted_exposure_roentgen = '{:,.2f}'.format(float(exposure_roentgen))
    formatted_exposure_per_xray_mR = '{:,.2f}'.format(float(exposure_per_xray_mR))

    # Print the result with HTML escaping
    print(f"Number of chest X-rays needed for ({escape(formatted_exposure_roentgen)}(R) / {escape(formatted_exposure_per_xray_mR)}(mR)): {escape(formatted_result)}")

    # Create an HTML string to display the result
    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>X-ray Calculation Result</title>
        <style>
            #xray 
            {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>
        <body>
            <h1>X-ray Calculation Result</h1>
            <p>Number of chest X-rays needed for 
                <p id="xray">{escape(formatted_exposure_roentgen)}(R) / {escape(formatted_exposure_per_xray_mR)}(mR): {escape(formatted_result)}</p>
            </p>
        </body>
    </html>
    """

    # Write the HTML string to an HTML file in 'append' mode
    with open('xray_result.html', 'a') as html_file:
        html_file.write(html_output)

    # Print a message indicating where the result has been saved
    print(f"\nResult has been saved to 'xray_result.html'")
