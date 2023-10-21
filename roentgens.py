xray = open('xray.txt', 'a')

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

    print(f"Number of chest X-rays needed for [{formatted_exposure_roentgen}(R) + {formatted_exposure_per_xray_mR}(mr)]: {formatted_result}")
    print(f"Number of chest X-rays needed for [{formatted_exposure_roentgen}(R) + {formatted_exposure_per_xray_mR}(mr)]: {formatted_result}",file=xray)