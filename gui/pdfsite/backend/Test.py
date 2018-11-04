from Main import *


pathToInputs = [r"C:\Users\nikhi\OneDrive\Desktop\hackathon\smartpdf\SmartPdf\backend\fedessa.docx"]
strPageList = ["*"]
waterMarkFilePath = r"C:\Users\nikhi\OneDrive\Desktop\hackathon\smartpdf\SmartPdf\backend\watermarker.pdf"
orientation = ["hi","hello"]
outputFilePath = r"C:\Users\nikhi\OneDrive\Desktop\hackathon\smartpdf\SmartPdf\backend\checkfede.pdf"

#apiWaterMark(inputFilePaths, strPageList, waterMarkFilePath, orientation, pathToOutputPdf)
#apiGenericMerge (pathToInputs, strPageList, orientation, outputFile)
apiWordToPdf (pathToInputs, outputFilePath)