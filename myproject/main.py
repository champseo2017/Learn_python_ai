from transformers import AutoTokenizer

# กำหนดชื่อ checkpoint ของโมเดลที่ต้องการ
model_ckpt = "distilbert-base-uncased"

# โหลด tokenizer จาก checkpoint
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

# ทดลองใช้ tokenizer กับข้อความตัวอย่าง
text = "I love NLP and transformers!"
encoded_text = tokenizer(text)

print(encoded_text)