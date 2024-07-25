def char_tokenize(text):
    """
    Tokenize a string at character level.
    """
    return list(text)

# ตัวอย่างการใช้งาน
text = "I love NLP!"
char_tokens = char_tokenize(text)
print(char_tokens)