import nltk
from utils.text import pdftotext

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

RESERVED_WORDS = [
    'school', 'college', 'univers', 'academy', 'faculty', 'institute', 'faculdades',
    'Schola', 'schule', 'lise', 'lyceum', 'lycee', 'polytechnic', 'kolej', 'ünivers', 'okul',
]

def extract_education(input_text):
    organizations = []
    
    # First, clean and tokenize the text properly
    input_text = input_text.replace('\n', ' ')  # Remove newlines, if any
    sentences = nltk.sent_tokenize(input_text)
    
    # Extract organization names using NLTK's Named Entity Recognition (NER)
    for sent in sentences:
        tokens = nltk.word_tokenize(sent)
        tagged_tokens = nltk.pos_tag(tokens)
        chunks = nltk.ne_chunk(tagged_tokens)
        
        for chunk in chunks:
            if isinstance(chunk, nltk.Tree) and chunk.label() == 'ORGANIZATION':
                org_name = ' '.join(c[0] for c in chunk.leaves())
                organizations.append(org_name)
    
    # Use regular expressions to match reserved words
    education = set()
    for org in organizations:
        org_lower = org.lower()
        for word in RESERVED_WORDS:
            if word.lower() in org_lower:
                education.add(org)
    
    return education
