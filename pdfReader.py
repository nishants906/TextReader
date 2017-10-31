import PyPDF2

def readfile(file):
    #open pdf file for reader
    file = open(file,"rb")
    reader = PyPDF2.PdfFileReader(file)

    fileData = ""
    for line in range(reader.numPages):
        pageData = reader.getPage(line)
        fileData += pageData.extractText()

    return fileData

