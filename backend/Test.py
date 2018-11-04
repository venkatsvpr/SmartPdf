from Main import *


pathToInputs = [r"C:\Users\nikhi\OneDrive\Desktop\hackathon\smartpdf\SmartPdf\backend\fedessa.docx",r"C:\Users\nikhi\OneDrive\Desktop\hackathon\smartpdf\SmartPdf\backend\Association1.pdf"]
strPageList = ["*", "1"]
orientation = ["hi","hello"]
outputFile = r"C:\Users\nikhi\OneDrive\Desktop\hackathon\smartpdf\SmartPdf\backend\fedessa.pdf"


apiGenericMerge (pathToInputs, strPageList, orientation, outputFile)
