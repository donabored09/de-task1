#Reading
import csv

with open('result.csv', 'r') as file:

    reader = csv.reader(file)
    file_out = open('result.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    writer = csv.writer(file)
    next(reader, None)
    for row in reader:
        if  "feb" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-02-01'
        elif "mar" in row[0] :
            s= row[0]
            row[0] = s[:4] +'-03-01'
        print(row)
