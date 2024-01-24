import csv

with open('data/neos.csv') as infile:
    reader = csv.DictReader(infile)
    i = 0
    for d in reader:
        print(d)
        i += 1
        if i == 2:
            break