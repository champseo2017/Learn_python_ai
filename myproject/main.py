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

input_ids = [token2idx[token] for token in tokenized_text]
# สร้าง list comprehension เพื่อแปลงแต่ละ token เป็นตัวเลข
# โดยใช้ token2idx dict ในการหาตัวเลขที่สอดคล้องกับแต่ละ token

print(input_ids)

# ผลลัพธ์เป็น list ของตัวเลขที่แทนแต่ละตัวอักษร เช่น
# [5, 14, 12, 8, 13, 11, 19, 11, 13, 10, 0, 17, 8, ...]