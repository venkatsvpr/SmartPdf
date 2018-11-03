from Globals import *

def expandPages (strPageList, maxPageCount):
   """
   :param strPageList:
   :return: list of page numbers
   """
   pages = strPageList.split(',')
   page_numbers = []
   for p in pages:
       if '-' in p:
           first_last = p.split('-')
           start = int(first_last[0])
           while(start <= int(first_last[1])):
               if start < maxPageCount:
                   page_numbers.append(start)
               start += 1
       else:
           page_numbers.append(int(p))
   return page_numbers

def WaterMark (inputPdfPath, waterMarkPath, pageList, outputPdfPath):
    """
    Add WaterMark to the inputFile for the pages in the pageList.
    Use the watermark from the waterMarkPath, the watermark pdf should have only one page
    Store the output on the outputPdfPath

    :param inputPdfPath: List of paths of input pdf files
    :param waterMarkPath: String to the watermark path
    :param pageList:  List of page numbers where we need the watermark
    :param outputPdfPath:
    :return:
    """
    inputFile = open(inputPdfPath, "rb")
    inFileReader = PyPDF2.PdfFileReader(inputFile)

    waterMarkFile = open(waterMarkPath, "rb")
    wmFileReader = PyPDF2.PdfFileReader(waterMarkFile)

    pdfWriter = PyPDF2.PdfFileWriter()
    if (pageList == None):
        pageSet = set(range(0,inFileReader.numPages))
    else:
        pageSet = set(pageList)

    for page in range(inFileReader.numPages):
        pageObject = inFileReader.getPage(page)
        if (page in PageSet):
            pageObject.mergePage(wmFileReader.getPage(0))
        pdfWriter.addPage(pageObject)

    inputFile.close()
    waterMarkFile.close()

    outputFile = open(outputPdfPath, "wb")
    pdfWriter.write(outputFile)
    outputFile.close()
    return

def MergePdf (pathToInputs, pageList, orientationDict, pathToOutputPdf):
    """
    TODO:
    Orientation
    Testing the method

    Open the input file, pick the pages passed, do the orientation and push it to output.
    :param pathToInputs: List of paths
    :param pageList:
    :param orientationDict:
    :param pathToOutputPdf:
    :return:
    """
    pdfWriter = PyPDF2.PdfFileWriter()
    outFile = open(pathToOutputPdf,"wb+")
    for inputFilePath,pages,orient in zip(pathToInputs, pageList, orientationDict):
        inputFileObject = open(inputFilePath, "rb")
        pdf = PyPDF2.PdfFileReader(inputFileObject)
        for page in pages:
            if (0 <= page < pdf.numPages):
                pageObject = pdf.getPage(page)
                #pageObject.rotateClockwise(90)
                pdfWriter.addPage(pageObject)
                pdfWriter.write(outFile)
        inputFileObject.close()
    outFile.close()



def DocToPdf (listOfDocFilePath, listOfOutputFilePath):
    """
    Convert the doc file in the doc-file path into a pdf file from
    listOfOutputFilePath
    :param listOfDocFilePath: Contains a list of doc files
    :param listOfOutputFilePath: Contains a list of pdf file (output
    :return:
    """
    wdFormatPDF = 17
    for i in range(0, len(listOfDocFilePath)):
        inputDocFilePath = listOfDocFilePath[i]
        outputDocFilePath = listOfOutputFilePath[i]
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(inputDocFilePath)
        doc.SaveAs(outputDocFilePath, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()

path = r"D:\Git_Projects\SmartPdf\1.pdf"
MergePdf ([path,path],[[3,4],[1,2,3]],["one","two"],"D:\Git_Projects\SmartPdf\out.pdf")