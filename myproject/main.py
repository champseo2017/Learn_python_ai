from huggingface_hub import list_datasets
from datasets import load_dataset

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion", trust_remote_code=True)


# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]

"""
เราสามารถดูได้ว่า Dataset กำลังใช้ data type อะไรในการเก็บข้อมูลผ่าน attribute ชื่อ features
"""
print(train_ds.features)
