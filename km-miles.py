def KM():
    """
    This function converts a given distance in kilometers to miles.
    It prompts the user to enter a distance in kilometers and then
    prints the equivalent distance in miles.
    """
    km = input(">>> ")
    km = float(km)  # Convert the input from string to float
    miles = km * 0.621371  # Perform the multiplication to convert km to miles
    print(f"{km} kilometers is equal to {miles} miles")
    return KM()
KM()