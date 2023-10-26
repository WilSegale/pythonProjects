from DontEdit import *
percentage = open("percentage.txt", "a")

def percent():
    part = float(input('''Enter the part of the % of the number '''))
    whole = float(input('''Enter the whole number '''))
    print(f"{part/whole*100 :,.2f}% is the number of {part} / {whole} * 100")
    print(f"{part/whole*100 :,.2f}% is the number of {part} / {whole} * 100",file=percentage)
percent()