import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # combining letters and digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

random_string = generate_random_string(100)  # Replace 10 with the desired length of the string
print(random_string)
 
