# นำเข้าไลบรารีที่จำเป็น
from transformers import AutoTokenizer

# โหลด tokenizer จากโมเดลภาษา (ในที่นี้ใช้ BERT เป็นตัวอย่าง)
# tokenizer คือเครื่องมือที่ช่วยตัดข้อความเป็นชิ้นๆ และแปลงเป็นตัวเลข
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# เริ่มต้นด้วยการแปลงข้อความเป็นตัวเลขที่คอมพิวเตอร์เข้าใจได้
text = "this is a test"  # ข้อความที่เราต้องการวิเคราะห์

# แปลงข้อความเป็นตัวเลข (tokenization)
# return_tensors="pt" คือการบอกให้ส่งผลลัพธ์ในรูปแบบ PyTorch tensor (ชุดตัวเลขที่ PyTorch ใช้)
# inputs จะเป็น dictionary ที่มีหลาย key เช่น 'input_ids' (รหัสตัวเลขของคำ) และ 'attention_mask' (บอกว่าควรสนใจตรงไหน)
inputs = tokenizer(text, return_tensors="pt")  

# แสดงขนาดของข้อมูลที่แปลงแล้ว
# inputs['input_ids'] คือตัวเลขแทนคำในประโยค
# .size() คือการดูขนาดของข้อมูล ผลลัพธ์เป็น [1, จำนวนโทเค็น]
# โดย 1 คือจำนวนประโยค และตัวเลขที่สองคือจำนวนโทเค็น (ชิ้นส่วนของข้อความ)
print(f"Input tensor shape: {inputs['input_ids'].size()}")

# แสดงตัวเลขที่แทนคำแต่ละคำ
print(f"Token IDs: {inputs['input_ids'][0]}")  # แสดงรหัสตัวเลขของแต่ละคำ

# ลองแปลงตัวเลขกลับเป็นคำเพื่อเข้าใจว่าตัดคำอย่างไร
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
print(f"Tokens: {tokens}")  # แสดงคำที่ถูกตัดแล้ว

# อธิบายความหมาย:
# [CLS] = สัญลักษณ์พิเศษที่เพิ่มเข้ามาตอนเริ่มประโยค
# [SEP] = สัญลักษณ์พิเศษที่เพิ่มเข้ามาตอนจบประโยค
# โทเค็นอื่นๆ คือคำต่างๆ ที่ถูกตัดแยกออกมาจากประโยค
