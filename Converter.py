import pythoncom
import win32com.client
from docx2pdf import convert


class ConverterUtils:
    #Инициализирует поток для ком порта
    def onThreadStart(threadIndex):
        pythoncom.CoInitialize()


    #Конвертирует DOC to PDF file
    def convertDocToPdf(self, inputFile, outputFile):
        convert(inputFile, outputFile)

    def saveFile(self, fileName, data):
        print(self)
        with open(fileName, "wb") as binary_file:
            # Write bytes to file
            binary_file.write(data)
            binary_file.close()

