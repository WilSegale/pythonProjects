import json

# Prompt the user to enter a message
message = input("Enter a message: ")

# Sample data (text) to write to a JSON file
data = {
    "message": message,
    "author": "WilSegale"
}

# Specify the file path where you want to save the JSON file
file_path = 'output.json'

# Writing data to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)  # indent for pretty-printing
