import random
import string
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion

class PathCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        directory = os.getcwd()
        for f in os.listdir(directory):
            if f.startswith(text):
                yield Completion(f, start_position=-len(text))

try:
    # Create a PromptSession with the custom completer
    session = PromptSession(completer=PathCompleter())

    # Simple REPL loop to demonstrate auto-completion
    while True:
        input_path = session.prompt('Enter file name: ')
        if input_path == 'exit':
            break

        length = int(input("Enter the desired length of the random string: "))
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        # Open the file in write mode to rewrite its content
        with open(input_path, "w") as file:
            file.write(random_string)
            
except KeyboardInterrupt:
    print("\n[-] Exiting...")