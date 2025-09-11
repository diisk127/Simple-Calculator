# Sprint2 Progress Simple Calculator

## งานที่ต้องทำในสัปดาห์นี้
---
* ฟังก์ชันคำนวณพื้นฐาน: add, subtract, multiply, divide
*	ระบบเมนูหลัก (calculator()) ที่ผู้ใช้สามารถเลือกฟังก์ชันและออกจากโปรแกรมได้
*	การปัดผลลัพธ์ทศนิยม 2 หลัก (round(...,2))
*	ตรวจสอบข้อผิดพลาดที่สำคัญ:
*	Division by zero
*	Choice ของเมนูไม่ถูกต้อง



## การแบ่งหน้าที่ทีม (2 คน)
---
### 1. ดิสก์ (Planner & Debugger)
* วางแผนการทำงาน และกำหนดขั้นตอนการพัฒนาโปรแกรม
* ออกแบบ โครงสร้างเมนูโปรแกรม และ flow การทำงานของเครื่องคิดเลข
* ช่วยแก้ไขข้อผิดพลาด (bugs) ที่เกิดจากฟังก์ชันหรือเมนู
* เขียนฟังก์ชันคำนวณ: add, subtract, multiply, divide และใส่ round เพื่อปัดทศนิยม

## ฟังก์ชันการคำนวณที่ดิสเขียน
```python

# ฟังก์ชันการบวก
def add(a,b):
  return round(a + b, 2)

# ฟังก์ชันการลบ
def subtract(a,b):
  return round(a - b, 2)

# ฟังก์ชันการคูณ
def multiply(a,b):
  return round(a * b, 2)

# ฟังก์ชันการหาร
def divide(a,b):
  if b == 0:  # ตรวจสอบตัวหาร = 0
    return "Cannot divide by zero"
  return round(a / b, 2)
```

คำอธิบายโค้ด:
* ฟังก์ชันแต่ละตัวรับค่า float 2 ตัว
*	round(...,2) ปัดผลลัพธ์เป็นทศนิยม 2 หลัก
*	ฟังก์ชัน divide ตรวจสอบ division by zero


### 2. ชมพู่ (Coder & Debugger)
* ลงมือเขียนโปรแกรมตามโครงสร้างที่วางไว้
* ออกแบบเมนูหลัก (calculator()), ตรวจสอบ input, จัดการ loop และ exit, ตรวจสอบ choice ผิดพลาด
* ทดสอบโปรแกรมเบื้องต้นและแก้ไขบั๊กจากผลการทดสอบ
* จัดการ การป้อนข้อมูล (input) ของผู้ใช้ให้ถูกต้อง
* ประสานงานกับดิสก์เพื่อแก้ไขปัญหาที่เกิดขึ้นระหว่างการรันโปรแกรม

## เมนูหลักและระบบ Loop ที่ชมเขียน

```python
# main function
def calculator():
  # ใช้ while True
  while True:
    print("-------- Calculator Menu --------")
    print("1. Add Function")
    print("2. Subtract Function")
    print("3. Multiply Function")
    print("4. Divide Function")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice not in ["1", "2", "3", "4", "5"]:
      print("Please try again.")
      continue


    # ตรวจสอบ Exit
    if choice == "5":
      print("End of the program...")
      break

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if choice == "1":
      print("Result: ", add(a, b))
    elif choice == "2":
      print("Result: ", subtract(a, b))
    elif choice == "3":
      print("Result: ", multiply(a, b))
    elif choice == "4":
      print("Result: ", divide(a, b))
    else:
      print("Invalid choice.")


calculator()
```

คำอธิบายโค้ด:
* while True ทำให้ผู้ใช้คำนวณต่อเนื่องได้
*	ตรวจสอบว่า choice อยู่ในเมนู 1–5
*	choice=5 → exit โปรแกรม
*	เรียกฟังก์ชันคำนวณตามตัวเลือก

## error ที่พบเจอและแก้ไข
---
1.	Division by zero
	*	ปัญหา: ถ้า b=0 โปรแกรม crash
	*	แก้ไข: เพิ่ม if b==0 ใน divide()
2.	Choice นอกช่วง 1–5
	*	ปัญหา: โปรแกรมทำงานผิดเมนู
	*	แก้ไข: ตรวจสอบ if choice not in ["1","2","3","4","5"]
3.	Rounding ไม่แม่นยำ
	*	ปัญหา: บางครั้ง float มีหลายทศนิยม
	*	แก้ไข: ใช้ round(...,2) ในทุกฟังก์ชัน

## Test case
---
	•	บวกเลขธรรมดา: 5 + 3 → 8.0
	•	ลบเลขทศนิยม: 10.5 - 4.25 → 6.25
	•	คูณเลข float: 2 × 3.5 → 7.0
	•	หารปกติ: 10 ÷ 2 → 5.0
	•	หารด้วย 0 → แสดงข้อความ “Cannot divide by zero”
	•	เลือกเมนูผิด → แสดงข้อความ “Please try again”
	•	เลือก exit → โปรแกรมหยุดทำงาน

 
