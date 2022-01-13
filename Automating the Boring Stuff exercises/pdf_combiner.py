#! python3
#  pdfcombiner.py - combines the pdf in a directory

import os, PyPDF2

os.makedirs('C:\\Pythoncode\\April batch', exist_ok = True)
os.chdir('C:\\Pythoncode\\April batch')

pdfWriter = PyPDF2.PdfFileWriter()

for filename in os.listdir():
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
PdfFileOutput = open(os.path.basename(os.getcwd())+'.pdf','wb')
pdfWriter.write(PdfFileOutput)
PdfFileOutput.close()

    
    


