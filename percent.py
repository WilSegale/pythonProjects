from DontEdit import *
def percent():
    part = int(float(input('''Enter the part of the % of the number ''')))
    whole = int(float(input('''Enter the whole number ''')))
    inputFile = input("would you like to put the number into a file so you can read it later? ")
    if inputFile in no:
        
        print(f"{part/whole*100 :,.2f}% of the number")
    elif inputFile in yes:
        
        print(f"{part/whole*100 :,.2f}% of the number",file=percent)

        
percent()