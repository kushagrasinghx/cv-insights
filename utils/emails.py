import re
from utils.text import doctotext,pdftotext
def extract_email(text):
    r=re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(text)