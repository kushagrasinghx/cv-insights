import docx2txt
import fitz

def doctotext(path):
    content=docx2txt.process(path)
    text=[line.replace('\t','') for line in content.split('\n') if line]
    text=' '.join(text)
    return text

def pdftotext(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
