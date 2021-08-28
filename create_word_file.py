from docx import Document
import glob
import os


def create_word_file(folder, fname, cleaned_content):
    with open(folder+"/"+fname+'.txt', 'wb') as f:
        f.write(cleaned_content)

    doc = Document()
     
    with open(folder+"/"+fname+'.txt', 'r', encoding='utf-8') as openfile:
        line = openfile.read()
        doc.add_paragraph(line)
        doc.save(folder+"/"+fname + ".docx")
        
    os.remove(folder+"/"+fname+'.txt')