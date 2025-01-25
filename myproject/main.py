# แบบฝึกหัดที่ 2-3: ข้อความส่วนตัว
# สร้างตัวแปรเก็บชื่อคน และพิมพ์ข้อความทักทาย
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)  # แสดงผล: Hello Eric, would you like to learn some Python today?

# แบบฝึกหัดที่ 2-4: รูปแบบชื่อ
# สร้างตัวแปรเก็บชื่อ แล้วแสดงผลในรูปแบบต่างๆ
name = "john smith"

# แสดงชื่อเป็นตัวพิมพ์เล็กทั้งหมด
print(name.lower())  # ผลลัพธ์: john smith

# แสดงชื่อเป็นตัวพิมพ์ใหญ่ทั้งหมด
print(name.upper())  # ผลลัพธ์: JOHN SMITH

# แสดงชื่อแบบขึ้นต้นด้วยตัวใหญ่
print(name.title())  # ผลลัพธ์: John Smith

# แบบฝึกหัดที่ 2-5: คำคมคนดัง
# พิมพ์คำคมพร้อมชื่อผู้พูด
author = "Albert Einstein"
quote = "Life is like riding a bicycle. To keep your balance, you must keep moving."
print(f'{author} once said, "{quote}"')
# ผลลัพธ์: Albert Einstein once said, "Life is like riding a bicycle. To keep your balance, you must keep moving."