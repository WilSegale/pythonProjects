import random

def generate_code(length):
    code = ""
    for i in range(length):
        if i != 0:
            code += ", "
        code += str(random.randint(0, 9))
    return code

print(generate_code(100))
