#! python3
#  sheetinverter.py - invert the row and column of the cells in the spreadsheet

import os, openpyxl

os.chdir('C:\\Pythoncode')

old_wb = openpyxl.load_workbook('inverter.xlsx')
old_sheet = old_wb.active


new_wb = openpyxl.Workbook()
new_sheet = new_wb.active


for col in range(1,old_sheet.max_column+1): #1,2,3
    for row in range(1,old_sheet.max_row+1): #1,2,3,...,9
        cellval = old_sheet.cell(row = row, column = col).value
        new_sheet.cell(row = col, column = row).value = cellval
new_wb.save('XD.xlsx')
        
        
        

        
        
        
