text = "Tokenizing text is a core task of NLP."

def word_tokenize(text):
    """
    Tokenize a string into words by splitting on whitespace.
    """
    return text.split()

tokenized_text = word_tokenize(text)
print(tokenized_text)