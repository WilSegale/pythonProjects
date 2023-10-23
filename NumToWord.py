def number_to_word(number):
    x = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero",
    }
    return x.get(number, "Number not found in the dictionary")

try:
    y = int(input("Enter a number: "))
    result = number_to_word(y)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
