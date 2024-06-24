from huggingface_hub import list_datasets
from datasets import load_dataset

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion", trust_remote_code=True)


# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]

"""
เรายังสามารถเข้าถึงชื่อคอลัมน์ทั้งหมดได้ผ่าน train_ds.column_names ซึ่งจะให้ผลลัพธ์เป็น list ของชื่อคอลัมน์ ['text', 'label']
"""
print(train_ds.column_names)
