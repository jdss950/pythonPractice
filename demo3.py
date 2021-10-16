# CSV Comma Separated Values a format for sotring data
# CSV Module

# Title,(separated by a comma) -> everything is represented as a string
# https://docs.google.com/spreadsheets/d/1G4sYrPtocF8eOoS4kEZtMQfMBTOc6luBu86Zm_vWiNA/edit#gid=1250910947

path = "C:\pygame1\CSV\google_stock_data.csv"
file = open(path)
for line in file:
    print(line)