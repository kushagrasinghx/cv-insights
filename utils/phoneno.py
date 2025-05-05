import re
from utils.text import pdftotext

def extract_phone_number(text):
    # Normalize all spacing in the resume text
    cleaned_text = re.sub(r'\s+', '', text)  # remove all whitespaces

    # Updated regex: handles optional country code and 10-digit numbers
    pattern = re.compile(r'(\+?\d{1,4})?(\d{10})')

    matches = pattern.findall(cleaned_text)
    if matches:
        # Join country code (if exists) + 10-digit number
        number = ''.join([part for part in matches[0] if part])
        return number

    return ""
