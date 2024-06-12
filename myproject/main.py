from huggingface_hub import list_datasets
from datasets import load_dataset

# แสดงรายชื่อชุดข้อมูลทั้งหมดที่มีอยู่
all_datasets = list(list_datasets())  # แปลง generator เป็น list
print(f"There are {len(all_datasets)} datasets currently available on the Hugging Face Hub")
print(f"The first 10 datasets are: {all_datasets[:10]}")

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion")

# แสดงโครงสร้างข้อมูลและรายละเอียดต่างๆ
"""
เมื่อดูภายใน `emotions` object จะเห็นว่ามีโครงสร้างคล้าย Python dictionary โดยแต่ละ key จะแทนชุดข้อมูลย่อย (data split) ที่แตกต่างกัน เช่น train, validation และ test เราสามารถใช้ syntax ของ dictionary เพื่อเข้าถึง split แต่ละตัวได้ เช่น DatasetDict({
    train: Dataset({
        features: ['text', 'label'],
        num_rows: 16000
    })
    validation: Dataset({
        features: ['text', 'label'],
        num_rows: 2000
    })
    test: Dataset({
        features: ['text', 'label'],
        num_rows: 2000
    })
})
"""
print(emotion_dataset)

# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]
print(f"Number of training samples: {len(train_ds)}")

# ดูตัวอย่างข้อมูลแรกในชุดฝึก
print(train_ds[0])
