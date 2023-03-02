import time
# Open the text file in read mode
file = open('DepressionQuotes.txt', 'r');
# Read the file line by line
line = file.readline()
while line:
    # Print the current line
    print(line)
    time.sleep(1)
    # Read the next line

# Close the file
file.close()
