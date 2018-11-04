# SmartPdf
A free smart pdf utility
APIs built

def apiMergeDocPdf (pathToInputs, strPageList, orientation, outputFile) :
    """
    Merges Doc and Pdfs, Internally converts the pdf to doc and performs merge
    :param pathToInputs: list of strings
    :param strPageList:   list of strings
    :param orientation:  orientation which is not currently used
    :param outputFile:   string, output file name
    :return:
    """

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

def apiMergePdf(inputFilePaths, pageLists, orientation, pathToOutputPdf):
    """
    merge the pdfs based on the pageList corresponding to the inputfile into one output file
    :param inputFilePaths:
    :param pageLists:
    :param orientation:
    :param pathToOutputPdf:
    :return:
    """

def apiWaterMark(inputFilePaths, strPageList, waterMarkFilePath, orientation, pathToOutputPdf):
    """
    Merges the Input File Paths based on the Pagelist, 
    add waterMark based on the waterMarkFile and the add the output to pathToOutput
    :param inputFilePaths: list of string paths
    :param strPageList:  list of strings representing areas of interest
    :param waterMarkFilePath: path to the watermark file
    :param orientation: orientation-- dont worry
    :param pathToOutputPdf: path to the output pdf file
    :return: 
    """
    
def apiWordToPdf (pathToInputs, outputFilePath):
    """
    Join all the input paths to one output PDF File
    :param pathToInputs: list of strings representing the path
    :param outputFilePath:
    :return:
    """
