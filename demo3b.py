import csv
#print(dir(csv)) # prints the directory - we can see the functions and classes the module has
path = r"C:\Users\jsuco\OneDrive\Desktop\CS\GitRe\pygame1\CSV\google_stock_data.csv.csv"
file = open(path, newline='') # new line argument  ensure csv module would work correctly across all platforms
reader = csv.reader(file)

header = next(reader) # The first line is the header
data = [row for row in header] # Read the remaining data
print(header)
print(data[0])