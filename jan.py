import csv
thisdict = {
 "jan" : "01-01",
 "feb" : "02-01",
 "mar" : "03-01",
 "apr" : "04-01",
 "may" : "05-01",
 "jun" : "06-01",
 "jul" : "07-01",
 "aug" : "08-01",
 "sep" : "09-01",
 "oct" : "10-01",
 "nov" : "11-01",
 "dec" : "12-01",
 }
with open('Dana.csv', 'r') as file:
    reader = csv.reader(file)
    file_out = open('Dana1.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    next(reader, None)
    for row in reader:
        #row[0]=row[0]
        #writer.writerow(row)
        row[0]=row[0][0:-3]+thisdict[row[0][5:8]]
        writer.writerow(row)
        #print(row[0][5:8])
        #print(thisdict[row[0][5:8]])
