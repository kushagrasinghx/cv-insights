import pandas as pd
import spacy
from utils.text import pdftotext

nlp = spacy.load('en_core_web_sm')

def extract_skills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]

    # reading the csv file
    data = pd.read_csv('skills.csv') 
    skills = data.columns.tolist()

    skillset = []

    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)

    # check for noun chunks (example: machine learning)
    for chunk in nlp_text.noun_chunks:
        chunk_text = chunk.text.lower().strip()
        if chunk_text in skills:
            skillset.append(chunk_text)

    cleaned = [i.capitalize() for i in set([i.lower() for i in skillset])]
    return ", ".join(cleaned)
