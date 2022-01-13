#! python3
#  multiplicationTable.py - Takes a number N from the command line
#  and creates an NxN multiplication table in Excel spreadsheet

import os, sys, openpyxl

os.chdir('C:\\Pythoncode')


if len(sys.argv) == 2:
    n_matrix = int(sys.argv[1])
else:
    print('Please enter a valud argument.')


# (r2,C2) = (R1,C2)*(r2,C1)    (r2,C3) = (R1,C3)*(r2,C1)  
# (r3,C2) = (R1,C2)*(r3,C1)    (r3,C3) = (R1,C3)*(r3,col1)  


wb = openpyxl.Workbook()
sheet = wb.active


for number in range(2, n_matrix+2):
    sheet.cell(row = 1, column = number).value = int(number-1)
    sheet.cell(row = number, column = 1).value = int(number-1)

    
lastcell = sheet.cell(row=sheet.max_row, column=sheet.max_column)
rcount = 2
for rowofcells in sheet['B2':lastcell.coordinate]: #Repeats 5 times
    ccount = 2
    for cellobj in rowofcells: #repeats 5 times
        cellobj.value = sheet.cell(row=1, column = ccount).value * sheet.cell(row=rcount, column = 1).value
        ccount = ccount + 1
    rcount = rcount + 1
        
        

wb.save('multiplicationtable.xlsx')

    
    
    
