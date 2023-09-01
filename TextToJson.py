# Python program to convert text
# file to JSON
import json

# the file to be converted
filename = 'data.txt'

# resultant dictionary
dict1 = {}

# fields in the sample file
fields = ['name', 'designation']

with open(filename) as fh:
    
    # count variable for employee id creation
    countLine = 1
    
    for line in fh:
        
        # reading line by line from the text file
        description = line.strip().split(None, len(fields))  # Use len(fields) as split limit
        
        # for automatic creation of id for each employee
        Loopvar = 0  # Moved Loopvar initialization here
        sno = 'emp' + str(Loopvar)
    
        # intermediate dictionary
        dict2 = {}
        for Loopvar in range(len(fields)):
            
            # creating dictionary for each employee
            if Loopvar < len(description):
                dict2[fields[Loopvar]] = description[Loopvar]
            else:
                dict2[fields[Loopvar]] = ""  # Fill missing fields with empty strings
        
        # appending the record of each employee to
        # the main dictionary
        dict1[sno] = dict2
        # Increment Loopvar here if needed

# creating json file    
out_file = open("output.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()
