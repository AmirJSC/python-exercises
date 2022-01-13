#! python3!
#  pdfsepator.py - separates a PDF into two PDF files; One for FBQ and the other for FBQ2.



import os, PyPDF2

os.chdir('C:\\Pythoncode\\MTG') #save the PDF in this directory


FBQ2_pages = [2] #If page 1 siya sa pdf, dapat page 0 siya pagbutang sa FBQ2_pages
FBQ1_pages = [] 
filename = str(input('What is the filename? ')) #Don't include the .pdf


pdfFile = open(filename +'.pdf', 'rb')  #opens the filename
pdfreader = PyPDF2.PdfFileReader(pdfFile) #create a PdfFileReader object
pdfwriter1 = PyPDF2.PdfFileWriter() #creare a PdfFileWriter object for FBQ1
pdfwriter2 = PyPDF2.PdfFileWriter() #creare a PdfFileWriter object for FBQ2
pageNumber = pdfreader.numPages #number of pages in the file


def missingPages(List):
    for x in range(pageNumber):
        if x not in List:
            FBQ1_pages.append(x)

missingPages(FBQ2_pages)


for pages in range(pageNumber):
    #for FBQ2
    if pages in FBQ2_pages:
        pdfwriter2.addPage(pdfreader.getPage(pages))
    else:
        pdfwriter1.addPage(pdfreader.getPage(pages))

FBQ1pdf = open('FBQ1 mtg requests.pdf','wb')
FBQ2pdf = open('FBQ2 mtg requests.pdf','wb')
pdfwriter1.write(FBQ1pdf)
pdfwriter2.write(FBQ2pdf)
pdfFile.close()
FBQ1pdf.close()
FBQ2pdf.close()



