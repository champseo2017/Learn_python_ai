from huggingface_hub import list_datasets
from datasets import load_dataset

# โหลดชุดข้อมูล "emotion"
emotion_dataset = load_dataset("emotion", trust_remote_code=True)

# แสดงโครงสร้างข้อมูลและรายละเอียดต่างๆ
"""
การใช้ trust_remote_code=True จะบอกกับไลบรารีว่าคุณเชื่อถือโค้ดที่มากับชุดข้อมูลนี้และยินยอมให้มันถูกดำเนินการ.
"""

# เข้าถึงข้อมูลฝึกซ้อม (training set)
train_ds = emotion_dataset["train"]
print(f"Number of training samples: {len(train_ds)}")

# ดูตัวอย่างข้อมูลแรกในชุดฝึก
print(train_ds["text"][:5])
