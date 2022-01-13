#! python3
#  textsheet.py

import os, openpyxl

os.chdir('C:\\Pythoncode\\tsfolder')

#opens a spreedsheet
wb = openpyxl.Workbook()
sheet = wb.active
col = 1


#Opens each of the file in the directory
for file in os.listdir('.'):
    textfile = open(file)
    text_list = textfile.readlines()
    for line in range(len(text_list)):
        sheet.cell(row = line+1, column = col).value = text_list[line]
    textfile.close()
    col += 1

wb.save('text2sheet.xlsx')
        
        
    
    




