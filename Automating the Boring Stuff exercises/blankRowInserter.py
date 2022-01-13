#! python3
#  blankRowInserter.py - takes 2 (N & M) intergers and 1 string as command line arguments
#  Starting at N, it inserts M rows

import os, openpyxl, sys

os.chdir('C:\\Pythoncode')

#Reads the arguments in the command line
if len(sys.argv) != 4:
    print('Invalid number of  arguments.')
    sys.exit(-1)


filename = sys.argv[3]
chosen_row = int(sys.argv[1]) #3
blank_row = int(sys.argv[2])  #2
  
#Copies all the cells from N to last row and put them to N + M
wb = openpyxl.load_workbook(filename)
sheet = wb.active
new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

maxrow = sheet.max_row
maxcol = sheet.max_column
lastcell = sheet.cell(row = maxrow, column = maxcol).coordinate
r = 0

if chosen_row > 1:
    for z in sheet['A1':sheet.cell(row=chosen_row-1,column=maxcol).coordinate]:
        for q in z:
            new_sheet[q.coordinate].value = q.value
            

for rowcells in sheet['A'+str(chosen_row):lastcell]:
    c = 1
    for cellobj in rowcells:
        m = sheet.cell(row=chosen_row+blank_row + r,column=c)
        new_sheet[m.coordinate].value = cellobj.value
        c = c + 1
    r = r + 1

new_wb.save('HAHA.xlsx')
