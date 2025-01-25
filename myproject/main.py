# แบบฝึกหัดที่ 2-6: คำคมคนดัง แบบที่ 2
# สร้างตัวแปรเก็บชื่อคนดังและข้อความแยกกัน
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "Life is like riding a bicycle. To keep your balance, you must keep moving."'
print(message)

# แบบฝึกหัดที่ 2-7: การลบช่องว่างในชื่อ
# \t คือการเว้นระยะแท็บ
# \n คือการขึ้นบรรทัดใหม่
name = "\t  John Smith\n   "

# พิมพ์ชื่อแบบมีช่องว่าง
print("ชื่อต้นฉบับ:")
print(name)

# ลบช่องว่างด้านซ้าย
print("\nลบช่องว่างด้านซ้าย:")
print(name.lstrip())

# ลบช่องว่างด้านขวา
print("\nลบช่องว่างด้านขวา:")
print(name.rstrip())

# ลบช่องว่างทั้งสองด้าน
print("\nลบช่องว่างทั้งสองด้าน:")
print(name.strip())

# แบบฝึกหัดที่ 2-8: การลบนามสกุลไฟล์
filename = 'python_notes.txt'
# ใช้ removesuffix() เพื่อลบ .txt ออก
clean_filename = filename.removesuffix('.txt')
print(f"ชื่อไฟล์เต็ม: {filename}")
print(f"ชื่อไฟล์ไม่มีนามสกุล: {clean_filename}")