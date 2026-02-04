import re

PARAGRAPH = "I can't believe it's not butter! NLP tools handle punctuation well. Tokenization is tricky sometimes."

def naive_tokenize(text):
    """Naive space-based tokenization."""
    return text.split()

def manual_tokenize(text):
    """Manual tokenization handling punctuation and clitics."""
    # Split punctuation as separate tokens
    tokens = re.findall(r"\w+|n't|'s|[.!?]", text)
    return tokens

def spacy_tokenize(text):
    """Tokenize using spaCy (optional dependency)."""
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        return [t.text for t in doc]
    except Exception as e:
        return ["spaCy not available:", str(e)]

def main():
    naive = naive_tokenize(PARAGRAPH)
    manual = manual_tokenize(PARAGRAPH)
    tool = spacy_tokenize(PARAGRAPH)

    print("Paragraph:\n", PARAGRAPH, "\n")
    print("Naive tokens:\n", naive, "\n")
    print("Manual tokens:\n", manual, "\n")
    print("Tool tokens:\n", tool, "\n")

    # Differences
    print("Differences (naive vs manual):")
    print(set(naive) ^ set(manual))

if __name__ == "__main__":
    main()