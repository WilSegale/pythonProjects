def number_to_word(number):
    x = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
    }

    if 0 <= number <= 100:
        if number <= 20 or number % 10 == 0:
            return x.get(number, "Number not found in the dictionary")
        else:
            tens = number // 10 * 10
            ones = number % 10
            return x[tens] + "-" + x[ones]
    else:
        return "Number not in the valid range (0-100)"

try:
    y = int(input("Enter a number: "))
    result = number_to_word(y)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
