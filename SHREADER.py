import random
import string
FILE = input("Enter the file name: ")
length = input("Enter the desired length of the string: ")
def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # combining letters and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

random_string = generate_random_string(int(length))  # Replace 10 with the desired length of the string

with open(FILE, 'w') as file:
    file.write(random_string)