import re

def split_sentences(text):
    abbreviations = {
        "et al", "e.g", "i.e", "Dr", "Mr", "Mrs", "Ms", "Jr", "Sr", "Inc", 
        "Ltd", "Co", "Corp", "Prof", "Assoc", "Asst", "PhD", "MBA"
    }
        
    # Pattern to match sentence endings followed by a space or end of the text
    sentence_endings = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'

    # Split the text using the sentence endings pattern
    sentences = re.split(sentence_endings, text)

    # Additional processing to handle abbreviations at the end of sentences
    processed_sentences = []
    for sentence in sentences:
        # If the sentence ends with an abbreviation, split it and rejoin
        if sentence.lower().rstrip().endswith(tuple(abbreviations)):
            # Find the position of the last period in the sentence
            last_period_index = len(sentence) - 1 - sentence.lower().rfind('.')
            # Split the sentence at the last period and rejoin the parts
            parts = sentence.rsplit('.', 1)
            processed_sentences.extend([parts[0] + '.', parts[1] + ' ' + parts[2] * (len(parts) > 2)])
        else:
            processed_sentences.append(sentence)

    return processed_sentences