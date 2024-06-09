"""
- ชื่อตัวแปรใช้ได้แค่ตัวอักษร ตัวเลข กับ _ 
- ขึ้นต้นด้วยตัวอักษรหรือ _ ได้ แต่ห้ามขึ้นต้นด้วยตัวเลข
- ห้ามเว้นวรรค แต่ใช้ _ แยกคำได้
- อย่าตั้งชื่อซ้ำกับ keyword และชื่อฟังก์ชันของ Python
- ชื่อควรสั้นแต่สื่อความหมายชัดเจน
- ระวังอย่าใช้ l (L เล็ก) กับ O (O ใหญ่) เพราะจะสับสนกับเลข 1, 0 ได้

การตั้งชื่อตัวแปรเป็นทักษะที่ต้องฝึกฝน ยิ่งเขียนโค้ดมากและอ่านโค้ดคนอื่นเยอะ ก็จะตั้งชื่อเก่งขึ้นเรื่อยๆ
"""

# name ดีกว่า n
name = "John"

# student_name ดีกว่า s_n
student_name = "Alice"

# name_length ดีกว่า length_of_persons_name 
name_length = len(name)

print(name)
print(student_name)  
print(name_length)