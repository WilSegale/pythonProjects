try:
    def c_to_f(c):
        f = (9/5) * c + 32
        return f

    while True:
        c = float(input("Enter the temperature in Celsius: "))
        print("Temperature in Fahrenheit: ", c_to_f(c))
except KeyboardInterrupt:
    print("\nExiting...")