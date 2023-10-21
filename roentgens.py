from DontEdit import *
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
    
    formatted_result = '{:,}'.format(result)
    formatted_exposure_roentgen = '{:,}'.format(float(exposure_roentgen))
    formatted_exposure_per_xray_mR = '{:,}'.format(float(exposure_per_xray_mR))
    print(f"Number of chest X-rays needed for {formatted_exposure_roentgen}(R) / {formatted_exposure_per_xray_mR}(mR): {formatted_result}")

    # Create an HTML string
    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>X-ray Calculation Result</title>
    </head>
    <body>
        <h1>X-ray Calculation Result</h1>
        <p>Number of chest X-rays needed for {formatted_exposure_roentgen}(R) / {formatted_exposure_per_xray_mR}(mR): {formatted_result}</p>
    </body>
    </html>
    """

    # Write the HTML string to an HTML file
    with open('xray_result.html', 'a') as html_file:
        html_file.write(html_output)

    print(f"\n{GREEN}[+]{RESET} Result has been saved to 'xray_result.html'")
