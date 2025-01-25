# ตั้งค่าข้อความเริ่มต้นที่มีช่องว่างทั้งด้านหน้าและด้านหลัง
text = ' python '

# วิธีที่ 1: ลบช่องว่างด้านขวา
# ผลลัพธ์จะได้: ' python'
right_stripped = text.rstrip()

# วิธีที่ 2: ลบช่องว่างด้านซ้าย
# ผลลัพธ์จะได้: 'python '
left_stripped = text.lstrip()

# วิธีที่ 3: ลบช่องว่างทั้งสองด้าน
# ผลลัพธ์จะได้: 'python'
both_sides_stripped = text.strip()

# ตัวอย่างการใช้งานจริง: การทำความสะอาดข้อมูลที่ผู้ใช้ป้อนเข้ามา
user_input = '   สวัสดี   '  # สมมติว่าผู้ใช้พิมพ์มีช่องว่างเยอะ
cleaned_input = user_input.strip()  # ลบช่องว่างออกให้เรียบร้อย
# ผลลัพธ์: 'สวัสดี'

print(cleaned_input)