import csv

dictlist =[]

with open('Votes2.csv', mode='r') as inp:
    reader = csv.DictReader(inp)

    for row in reader:
        dictlist.append(row)

