from html import escape

def calculate_xray_count(exposure_roentgen, exposure_per_xray_mR):
    try:
        exposure_roentgen = float(exposure_roentgen)
        exposure_per_xray_mR = float(exposure_per_xray_mR)
        
        # Convert exposure_roentgen to milliroentgens
        exposure_mR = exposure_roentgen * 1000
        
        # Calculate the number of chest X-rays
        xray_count = exposure_mR / exposure_per_xray_mR
        
        return xray_count
    except ValueError:
        return "Invalid input. Please enter valid numeric values."

if __name__ == "__main__":
    exposure_roentgen = input("Enter the desired exposure in roentgens (R): ")
    exposure_per_xray_mR = input("Enter the exposure per chest X-ray in milliroentgens (mR): ")

    result = calculate_xray_count(exposure_roentgen, exposure_per_xray_mR)
    
    formatted_result = '{:,.2f}'.format(result)  # Format result as a float with 2 decimal places
    formatted_exposure_roentgen = '{:,.2f}'.format(float(exposure_roentgen))
    formatted_exposure_per_xray_mR = '{:,.2f}'.format(float(exposure_per_xray_mR))
    print(f"Number of chest X-rays needed for {escape(formatted_exposure_roentgen)}(R) / {escape(formatted_exposure_per_xray_mR)}(mR): {escape(formatted_result)}")
    # Create an HTML string
    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>X-ray Calculation Result</title>
        <style>
            #xray {{ color: green; }}
        </style>
    </head>
    <body>
        <h1>X-ray Calculation Result</h1>
        <p id="xray">Number of chest X-rays needed for {escape(formatted_exposure_roentgen)}(R) / {escape(formatted_exposure_per_xray_mR)}(mR): {escape(formatted_result)}</p>
    </body>
    </html>
    """

    # Write the HTML string to an HTML file
    with open('xray_result.html', 'a') as html_file:
        html_file.write(html_output)

    print(f"\nResult has been saved to 'xray_result.html'")
