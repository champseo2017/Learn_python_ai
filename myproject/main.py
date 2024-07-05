"""
เมื่อทำงานกับสตริง (ข้อความ) อีกหนึ่งงานที่พบบ่อยคือการลบคำนำหน้า (prefix) ออกจากสตริง ยกตัวอย่างเช่น URL ที่มีคำนำหน้าทั่วไปอย่าง 'https://'
"""

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
# ผลลัพธ์: 'nostarch.com'