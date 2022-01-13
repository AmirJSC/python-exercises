#! python3
#  removeCsvHeader.py - Removes the header from all the CSV files in the current working directory

import os, csv

os.chdir('C:\\Pythoncode')
os.makedirs('headerRemoved',exist_ok = True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    csvRows = []
    csvFile = open(csvFilename)
    csvReader =  csv.reader(csvFile)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue
        csvRows.append(row)
    csvFile.close()

    csvFile = open(os.path.join('headerRemoved',csvFilename),'w',newline ='')
    csvWriter = csv.writer(csvFile)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFile.close()
