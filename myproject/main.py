from transformers import AutoTokenizer

# 1. เรียกใช้ Tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# 2. Tokenize ข้อความ
text = "Tokenizing text is a core task of NLP."
encoded_text = tokenizer(text)

print("Encoded text:")
print(encoded_text)

# 3. แปลง Token IDs กลับเป็น Tokens
tokens = tokenizer.convert_ids_to_tokens(encoded_text.input_ids)

print("\nTokens:")
print(tokens)

# 4. Decode Tokens กลับเป็นข้อความ
decoded_text = tokenizer.decode(encoded_text.input_ids)

print("\nDecoded text:")
print(decoded_text)

# 5. tokenize และ decode หลายประโยค
batch_sentences = [
    "Tokenization is a core task of NLP.",
    "BERT is a popular transformer-based model.",
    "Hugging Face provides many pretrained tokenizers."
]
encoded_inputs = tokenizer(batch_sentences, padding=True, truncation=True, return_tensors="pt")

print("\nEncoded inputs:")
print(encoded_inputs)