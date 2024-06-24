from huggingface_hub import list_datasets
from datasets import load_dataset

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion", trust_remote_code=True)


# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]

"""
สามารถเข้าถึงข้อมูลหลายแถวพร้อมกันได้ด้วยการใช้ slice

train_ds[:5] หมายถึงการเข้าถึงข้อมูล 5 แถวแรก ซึ่งผลลัพธ์ที่ได้จะเป็น dictionary ที่มี value เป็น list ของข้อมูลใน 5 แถวนั้น
"""
print(train_ds[:5])
