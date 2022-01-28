import csv

# the list of dictionaries, one dictionary per state
dictlist =[]


#we read the csv file row by row, create a dictionary and append it to the list
with open('Votes2.csv', mode='r') as inp:
    reader = csv.DictReader(inp)

    for row in reader:
        dictlist.append(row)

