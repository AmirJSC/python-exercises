#! python3
#  pdfparanoia.py

import os, PyPDF2, sys

os.chdir('C:\\Pythoncode\\xd')

try:
    password = ' '.join(sys.argv[1:])
    if len(sys.argv) < 2:
        raise ValueError('Argument should be equal to or greater than 2.')
except ValueError as error:
    print(error)
   

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        file = open(filename, 'rb')
        filereader = PyPDF2.PdfFileReader(file)
        filewriter = PyPDF2.PdfFileWriter()

        
        for pageNum in range(filereader.numPages):
            filewriter.addPage(filereader.getPage(pageNum))

    filewriter.encrypt(password)
    outputFile = open(os.path.splitext(filename)[0] + '_encrypted.pdf','wb')
    filewriter.write(outputFile)
    outputFile.close()
    file.close()

    try:
        newfile =  open(os.path.splitext(filename)[0] + '_encrypted.pdf','rb')
        newfilereader = PyPDF2.PdfFileReader(newfile)
        if newfilereader.isEncrypted == True:
            print(filename + 'has been encrypted.')
    finally:
        newfile.close()
    
