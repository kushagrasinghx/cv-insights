import spacy
from utils.text import pdftotext
from spacy.matcher import Matcher

nlp=spacy.load('en_core_web_sm')

matcher=Matcher(nlp.vocab)

def extract_name(text):
    nlp_text=nlp(text)
    pattern=[{'POS':'PROPN'},{'POS':'PROPN'}]
    matcher.add('NAME',[pattern])
    matches=matcher(nlp_text)

    for match,start,end in matches:
        span=nlp_text[start:end]
        return span.text
    