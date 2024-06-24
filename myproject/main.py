from huggingface_hub import list_datasets
from datasets import load_dataset

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion", trust_remote_code=True)


# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]

"""
เข้าถึงข้อมูลแถวเดียว เช่น train_ds[0] เราจะได้ข้อมูลออกมาในรูปแบบของ dictionary ที่มี key เป็นชื่อคอลัมน์ และ value เป็นข้อมูลในแถวนั้นๆ
"""
print(train_ds[0])
