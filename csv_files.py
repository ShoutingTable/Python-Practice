import csv

with open('sample-input-1.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)