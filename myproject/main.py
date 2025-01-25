# ตัวอย่างโค้ดที่มีข้อผิดพลาด
# Python จะแสดงข้อความผิดพลาดตรงที่มีเครื่องหมาย ^ ด้านล่าง
# message = 'One of Python's strengths is its diverse community.'
#                          ^ ตำแหน่งที่เกิดข้อผิดพลาด

# ข้อความแสดงความผิดพลาดที่จะเห็น:
# SyntaxError: unterminated string literal (detected at line 1)
# แปลว่า: มีข้อผิดพลาดเกี่ยวกับการเขียนข้อความไม่ถูกต้องตามหลักไวยากรณ์

# วิธีแก้ไขที่ถูกต้อง - มี 3 วิธี:
# วิธีที่ 1: ใช้เครื่องหมาย " " แทน ' '
message = "One of Python's strengths is its diverse community."

# วิธีที่ 2: ใช้ \' แทน '
message = 'One of Python\'s strengths is its diverse community.'

# วิธีที่ 3: ใช้ """ """ สำหรับข้อความที่มีทั้ง ' และ "
message = """One of Python's "strengths" is its diverse community."""

print(message)