from huggingface_hub import list_datasets
from datasets import load_dataset

text = "Tokenizing text is a core task of NLP."
"""
Python เพราะใต้ฮู้ด string (str) นั้นจะเป็นอาเรย์อยู่แล้ว เราจึงสามารถเปลี่ยนเป็น list เพื่อให้ได้ character token แต่ละตัวได้ทันที
"""

tokenized_text = list(text)
# เปลี่ยน string ให้เป็น list โดย Python จะแยกเป็น list ที่มีสมาชิกเป็นแต่ละตัวอักษรใน string โดยอัตโนมัติ

print(tokenized_text)