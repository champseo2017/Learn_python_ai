from huggingface_hub import list_datasets
from datasets import load_dataset

text = "Tokenizing text is a core task of NLP."
"""

"""

tokenized_text = list(text)

token2idx = {ch: idx for idx, ch in enumerate(sorted(set(tokenized_text)))}
# สร้าง dictionary ที่แมป character token ไปเป็นตัวเลขเฉพาะ (index) 
# - ใช้ set() กับ tokenized_text เพื่อเอาเฉพาะตัวซ้ำ แล้วเรียงลำดับด้วย sorted()  
# - ใช้ enumerate() เพื่อสร้างคู่ของ index กับ character
# - สร้าง dict comprehension โดยใช้ชื่อ ch เป็น key และ idx เป็น value

print(token2idx)

# ผลลัพธ์เป็น dictionary ที่แมปแต่ละตัวอักษรไปเป็นตัวเลขเฉพาะ เช่น 
# {' ': 0, '.': 1, 'L': 2, 'N': 3, 'P': 4, 'T': 5, ... }