# ตัวอย่างการใช้ removeprefix()

# สร้างตัวแปรเก็บ URL
nostarch_url = 'https://nostarch.com'

# ใช้ removeprefix() เพื่อลบ 'https://' ออก
simple_url = nostarch_url.removeprefix('https://')

# แสดงผลลัพธ์
print(f"URL เดิม: {nostarch_url}")
print(f"URL ที่ลบ 'https://' ออกแล้ว: {simple_url}")

# ข้อความเดิมไม่เปลี่ยนแปลง
print(f"URL เดิมยังคงเหมือนเดิม: {nostarch_url}")