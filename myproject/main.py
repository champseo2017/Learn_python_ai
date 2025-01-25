# ตัวอย่างการลบ https:// ออกจาก URL

# สร้างตัวแปรเก็บ URL เต็ม
nostarch_url = 'https://nostarch.com'

# ใช้ removeprefix() เพื่อลบ 'https://' ออก
# วิธีใช้: ชื่อตัวแปร.removeprefix('คำที่ต้องการลบ')
clean_url = nostarch_url.removeprefix('https://')
# ผลลัพธ์: 'nostarch.com'

# ตัวอย่างการใช้งานอื่นๆ
# ลบคำนำหน้าชื่อออก
full_name = 'นายสมชาย ใจดี'
name_only = full_name.removeprefix('นาย')
# ผลลัพธ์: 'สมชาย ใจดี'

# ลบรหัสนำหน้าสินค้า
product_code = 'PRD-12345'
number_only = product_code.removeprefix('PRD-')
# ผลลัพธ์: '12345'

print(clean_url)
print(name_only)
print(number_only)
