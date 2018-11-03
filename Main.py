from Globals import *

def expandPages (strPageList):
    """
    :param strPageList:
    :return: list of page numbers
    """

def MergePdf (pathToInputs, pageList, orientationDict, pathToOutputPdf):
    """
    TODO:
    Orientation
    Testing the method

    Open the input file, pick the pages passed, do the orientation and push it to output.
    :param pathToInputs:
    :param pageList:
    :param orientationDict:
    :param pathToOutputPdf:
    :return:
    """
    pdfWriter = PyPDF2.PdfFileWriter()
    for inputFilePath,pages,orient in zip(pathToInputs, pageList, orientationDict):
        try:
            inputFileObject = open (inputFilePath,"rb")
            pdf = PyPDF2.PdfFileReader(inputFileObject)
            for page in pages:
                if (0 <= page < pdf.numPags):
                    pageObject = pdf.getPage(page)
                    #pageObject.rotateClockwise(90)
                    pdfWriter.addPage(pageObject)
            inputFileObject.close()
        except:
            continue
    try:
        outFile = open(pathToOutputPdf,"wb")
        pdfWriter.write(outFile)
        outFile.close()
    except:
        continue

