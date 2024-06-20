import random
import string
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion # type: ignore

class PathCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        directory = os.getcwd()
        for f in os.listdir(directory):
            if f.startswith(text):
                yield Completion(f, start_position=-len(text))

# Create a PromptSession with the custom completer
session = PromptSession(completer=PathCompleter())

# Simple REPL loop to demonstrate auto-completion
while True:
    input_path = session.prompt('Enter file name: ')
    if input_path == 'exit':
        break
    print(f'You entered: {input_path}')

try:
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
        
except KeyboardInterrupt:
    print("\n[-] Exiting...")