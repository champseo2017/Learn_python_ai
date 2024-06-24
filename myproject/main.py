from huggingface_hub import list_datasets
from datasets import load_dataset

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion", trust_remote_code=True)


# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]

"""
สามารถเข้าถึงข้อมูลทั้งคอลัมน์ได้โดยระบุชื่อคอลัมน์ 

เข้าถึงข้อมูลในคอลัมน์ 'text' โดยเอาแค่ 5 แถวแรก ก็จะได้ list ของข้อความ 5 ข้อความแรกในคอลัมน์นั้น

"""
print(train_ds["text"][:5])
