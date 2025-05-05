import re
from utils.text import doctotext, pdftotext

def extract_email(text):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    matches = r.findall(text)
    return ", ".join(matches) if matches else ""
