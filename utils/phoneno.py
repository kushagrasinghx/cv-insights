import re
from utils.text import pdftotext
def extract_phone_number(text):
    r = re.compile(r'(\+?[0-9]{1,4})?(\(?\d{1,4}\)?)?([2-9][0-9]{2})?([2-9][0-9]{2})?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?')
    phone=r.findall(text)
    if phone:
        number = ''.join([part for part in phone[0] if part])
    return number
