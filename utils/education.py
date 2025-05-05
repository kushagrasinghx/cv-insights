import nltk
import re
from utils.text import pdftotext

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

RESERVED_WORDS = [
    'school', 'college', 'university', 'academy', 'faculty', 'institute', 'faculdades',
    'schola', 'schule', 'lise', 'lyceum', 'lycee', 'polytechnic', 'kolej', 'univers', 'okul',
]

GENERIC_TERMS = {'university', 'institute', 'college', 'school', 'academy'}

def extract_education(input_text):
    organizations = set()
    lines = input_text.split('\n')

    # NER-based detection
    for line in lines:
        sentences = nltk.sent_tokenize(line)
        for sent in sentences:
            tokens = nltk.word_tokenize(sent)
            tagged_tokens = nltk.pos_tag(tokens)
            chunks = nltk.ne_chunk(tagged_tokens)

            for chunk in chunks:
                if isinstance(chunk, nltk.Tree) and chunk.label() == 'ORGANIZATION':
                    org_name = ' '.join(c[0] for c in chunk.leaves())
                    if any(word in org_name.lower() for word in RESERVED_WORDS):
                        organizations.add(org_name.strip())

    # Fallback regex-based detection
    for line in lines:
        line_clean = line.strip()
        if any(word in line_clean.lower() for word in RESERVED_WORDS):
            if 5 < len(line_clean.split()) < 15 and line_clean.count(',') <= 2:
                organizations.add(line_clean)

    # Clean and filter out overly generic entries
    cleaned = []
    for org in organizations:
        org_clean = org.strip()
        if org_clean.lower() not in GENERIC_TERMS:
            cleaned.append(org_clean)

    return ", ".join(sorted(set(cleaned)))
