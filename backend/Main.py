from Globals import *

TEMPORARY_DIR_PATH = None

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
    Output  [0,1,2,3,9,3] as page ids
    """
    page_numbers = []
    if strPageList == "*":
        start = 0
        while(start < maxPageCount):
            page_numbers.append(start)
            start += 1
        return page_numbers
    pages = strPageList.split(',')
    for p in pages:
        if '-' in p:
            first_last = p.split('-')
            start = int(first_last[0]) - 1
            while(start < int(first_last[1])):
                if ((start < maxPageCount) and (start >= 0)):
                    page_numbers.append(start)
                start += 1
        else:
            if ((int(p) > 0) and (int(p) < maxPageCount)):
                page_numbers.append(int(p) - 1)
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
    return

def getMaxPageCount (inputFilePath):
    """
    Returns the Max Page Count of an input file

    :param inputFilePath:
    :return:
    """
    inputFilePath = os.path.normpath(inputFilePath)
    inputFile = open(inputFilePath,"rb")
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
    pageList = expandPages (strSplitRange, getMaxPageCount(inputFilePath))
    MergePdf ([inputFilePath], pageList, None, outputFilePath)
    return

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
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(inputDocFilePath)
        outputDocFilePath = listOfOutputFilePath[i]
        doc.SaveAs(outputDocFilePath, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
    return

def isFilePdf (filePath):
    """
    checks and returns True/False if the filename passed on filePath is a actually a pdf file
    :param filePath: string of the path of the file
    :return: True/False
    """
    pathString = magic.from_file(filePath, mime=True)
    if "/" in pathString:
        pathString = pathString.split("/")[1]
        if "." in pathString:
            pathString = pathString.split(".")
            pathString = pathString[len(pathString)-1]
        if pathString == "pdf":
            return True
        else:
            return False
    else:
        return False
def isFileDoc (filePath):
    """
    checks and returns True/False if the filename passed on filePath is a actually a doc file
    :param filePath: string .. of path of the file
    :return:  True/False
    """
    pathString = magic.from_file(filePath, mime=True)
    if "/" in pathString:
        pathString = pathString.split("/")[1]
        if "." in pathString:
            pathString = pathString.split(".")
            pathString = pathString[len(pathString)-1]
        if pathString == "document":
            return True
        else:
            return False
    else:
        return False

def genTempFileName (filePath):
    """
    Generate a temporary file based on the file path passed
    :param filePath: stringof a path
    :return: string of a temporary pdf file generated
    """
    global TEMPORARY_DIR_PATH
    if not TEMPORARY_DIR_PATH:
        TEMPORARY_DIR_PATH = tempfile.mkdtemp()
    id = hashlib.md5(filePath.encode('utf-8')).hexdigest()
    return TEMPORARY_DIR_PATH + "\\" + str(id)+".pdf"
    
def deleteFiles (listOfFilesToDelete):
    """
    Delete the list of files passed to this
    :param listOfFilesToDelete:
    :return: Nothing
    """

def apiMergeDocPdf (pathToInputs, strPageList, orientation, outputFile) :
    """
    Merges Doc and Pdfs, Internally converts the pdf to doc and performs merge
    :param pathToInputs: list of strings
    :param strPageList:   list of strings
    :param orientation:  orientation which is not currently used
    :param outputFile:   string, output file name
    :return:
    """
    listOfPdfs = []
    tempPdfFile = []
    for path in pathToInputs:
        if (isFileDoc(path)):
            tempFile = genTempFileName(path)
            tempPdfFile.append(tempFile)
            DocToPdf([path], [tempFile])
        else:
            tempFile = path
        listOfPdfs.append(tempFile)
    apiMergePdf(listOfPdfs, strPageList, orientation, outputFile)
    deleteFiles (tempPdfFile)
    return

def apiGenericMerge (pathToInputs, strPageList, orientation, outputFile) :
    """
    Generic Merge function that is called from the GUI,
    internally converts file appropriately and merges it to the output file
    :param pathToInputs:  list of strings
    :param strPageList:   list of strings
    :param orientation:   doesnt matter
    :param outputFile:     string of the output file name
    :return:
    """
    pageList = []
    if (all([isFilePdf(path) for path in pathToInputs])):
        apiMergePdf (pathToInputs, strPageList, orientation, outputFile)
    elif (all([isFilePdf(path) or isFileDoc(path) for path in pathToInputs])):
        apiMergeDocPdf (pathToInputs, strPageList, orientation, outputFile)
    else:
        print("Invalid input format.")


def apiMergePdf(inputFilePaths, pageLists, orientation, pathToOutputPdf):
    """
    merge the pdfs based on the pageList corresponding to the inputfile into one output file
    :param inputFilePaths:
    :param pageLists:
    :param orientation:
    :param pathToOutputPdf:
    :return:
    """
    pageList = []
    for inputFileId in range(0,len(inputFilePaths)):
        pages = expandPages (pageLists[inputFileId], getMaxPageCount (inputFilePaths[inputFileId]))
        pageList.append(pages)
    MergePdf(inputFilePaths, pageList, orientation, pathToOutputPdf)
    return
