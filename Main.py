from Globals import *

def expandPages (strPageList):
    """
    :param strPageList:
    :return: list of page numbers
    """

def MergePdf (pathToInputs, pageList, orientationDict, pathToOutputPdf):
    pdfWriter = PyPDF2.PdfFileWriter()
    for inputFilePath,pages,orient in zip(pathToInputs, pageList, orientationDict):
        inputFileObject = open (inputFilePath,"rb")
        pdf = PyPDF2.PdfFileReader(inputFileObject)
        for page in pages:
            if (0 <= page < pdf.numPags):
                pdfWriter.addPage(pdf.getPage(page))
        inputFileObject.close()
    outFile = open(pathToOutputPdf,"wb")
    pdfWriter.write(outFile)
    outFile.close()