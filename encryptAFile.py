import random
import string
print("Input a file name.")
file_path = input(">>> ")  # Replace with your file's path

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

length = int(input("Enter the desired length of the random string: "))
random_string = generate_random_string(length)

# Open the file in write mode to rewrite its content
with open(file_path, "w") as file:
    file.write(random_string)