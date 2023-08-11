file_path = "test.txt"  # Replace with your file's path

new_text = "This is the new text that will replace the old content."

with open(file_path, "w") as file:
    file.write(new_text)

print("File has been rewritten with new content.")

