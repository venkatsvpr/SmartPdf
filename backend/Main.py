from Globals import *

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
        if (page in pageSet):
            pageObject.mergePage(wmFileReader.getPage(0))
        pdfWriter.addPage(pageObject)
    outputFile = open(outputPdfPath, "wb")
    pdfWriter.write(outputFile)

    outputFile.close()
    inputFile.close()
    waterMarkFile.close()
    return

def expandPages (strPageList, maxPageCount):
   """
   :param strPageList:
   :return: list of page numbers
   Input "1,2-4,10,4"
   Output  [1,2,3,4,10,4]
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

def MergePdf (pathToInputs, pageList, orientationDict, pathToOutputPdf):
    """
    TODO:
    Orientation, Testing the method
    Open the input file, pick the pages passed, do the orientation and push it to output.
    :param pathToInputs: List of path to input files
    :param pageList: use the output of expandPages
    :param orientationDict: Ignore
    :param pathToOutputPdf: path to outputfile
    :return:
    """
    pdfWriter = PyPDF2.PdfFileWriter()
    outFile = open(pathToOutputPdf,"wb+")
    for inputFilePath,pages in zip(pathToInputs, pageList):
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

def getMaxPageCount (inputFilePath):
    """
    Returns the Max Page Count of an input file
    :param inputFilePath:
    :return:
    """
    inputFile = open(inputFilePath, "rb")
    inFileReader = PyPDF2.PdfFileReader(inputFile)
    numberOfPages = inFileReader.numPages
    inputFile.close()
    return numberOfPages

def SplitPagesFromPdfFile (inputFilePath, strSplitRange, outputFilePath):
    """
    Split a part of the Input file and creates another PDF File
    :param inputFilePath: Input File path
    :param strSplitRange: Range of the split in string format
    :param outputFilePath: Output File Path
    :return: Nothing
    """
    pageList = expandPages (strSplitRange, getMaxPageCount(inputFilePath)
    MergePdf ([inputFilePath], pageList, None, outputFilePath)

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
    return
path = r"D:\Git_Projects\SmartPdf\1.pdf"
MergePdf ([path,path],[[3,4],[1,2,3]],["one","two"],"D:\Git_Projects\SmartPdf\out.pdf")