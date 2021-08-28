import os
import pdfplumber
from docx2pdf import convert

def doc_to_pdf(directory):
    for name in os.listdir(directory):
        try:
            convert(name)
        except:
            print("Skipped: ",name)
            
    return 
path = input("Enter the file path:\t")

try:
    doc_to_pdf(path)
    
except:
    print("invalid path")