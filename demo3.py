# CSV Comma Separated Values a format for sotring data
# CSV Module

# Title,(separated by a comma) -> everything is represented as a string
# https://docs.google.com/spreadsheets/d/1G4sYrPtocF8eOoS4kEZtMQfMBTOc6luBu86Zm_vWiNA/edit#gid=1250910947

#r converts normal string to raw string
path = r"C:\Users\jsuco\OneDrive\Desktop\CS\GitRe\pygame1\CSV\google_stock_data.csv.csv"
#file = open(path)
#for line in file:
#    print(line)

# list comprehension
#lines = [line for line in open(path)]

#print(lines[0])
#print(lines[1])

#print(lines[0].strip()) # strip() method can be use to remove any leading or trailing white space.
#print(lines[0].strip().split(',')) # split method to divide the string into smaller pieces.

dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])
# Why use the csv module ( some movie or book names contain comas)
