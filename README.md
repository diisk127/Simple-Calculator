

---

#  แผนการดำเนินงาน Sprint 1

**โครงงาน:** Simple Calculator (เครื่องคิดเลขอย่างง่าย)
**สมาชิกกลุ่ม:**

* ชม (Planner)
* ดิส (Coder)
* ชม และ ดิส (Debuggers)

---

## 1. เป้าหมายของ Sprint 1

* กำหนดขอบเขตโครงงานและคุณสมบัติหลัก
* พัฒนาโปรแกรมเครื่องคิดเลขเวอร์ชันแรกที่สามารถคำนวณบวก ลบ คูณ หาร ได้
* ทดสอบการทำงานของโปรแกรมและแก้ไขข้อผิดพลาดที่พบ

---

## 2. การแบ่งหน้าที่

* **ชม (Planner):** วางแผนและกำหนดคุณสมบัติของเครื่องคิดเลข จัดทำตารางการทำงานในสัปดาห์
* **ดิส (Coder):** เขียนโค้ดตามที่กำหนด โดยรองรับการบวก ลบ คูณ หาร และตรวจสอบการหารด้วยศูนย์
* **ชม และ ดิส (Debuggers):** ร่วมกันทดสอบการทำงานของโปรแกรมกับข้อมูลตัวอย่าง หาข้อผิดพลาดและแก้ไข

---

## 3. การดำเนินงานในสัปดาห์ที่ 1

* **วันที่ 1–2:** ชม กำหนดความต้องการของโครงงาน (Basic calculator +, -, \*, /) และจัดทำแผนการทำงาน
* **วันที่ 3–4:** ดิส เขียนโค้ดเวอร์ชันแรกของเครื่องคิดเลข โดยใช้ภาษา Python 
* **วันที่ 5:** ชม และ ดิส ทำการทดสอบโปรแกรมกับตัวเลขต่าง ๆ เช่น บวกเลขบวก ลบกับเลขติดลบ และการหารด้วยศูนย์
* **วันที่ 6:** แก้ไขจุดบกพร่อง เช่น การจัดการกรณีหารด้วยศูนย์ และปรับการแสดงผลให้เหมาะสม
* **วันที่ 7:** สรุปผลการทำงานและจัดทำรายงาน Sprint 1

---

## 4. ปัญหาและการแก้ไข

* **ปัญหา:** พบข้อผิดพลาดเมื่อผู้ใช้ป้อนศูนย์เป็นตัวหาร

  * **การแก้ไข:** เพิ่มเงื่อนไขตรวจสอบ หากตัวหารเป็นศูนย์ ให้โปรแกรมแสดงข้อความ “ไม่สามารถหารด้วยศูนย์ได้”
* **ปัญหา:** การแสดงผลยังไม่เป็นระเบียบในเวอร์ชันแรก

  * **การแก้ไข:** ปรับรูปแบบการแสดงผลให้อ่านง่ายขึ้น เช่น `ผลลัพธ์ = …`

---

## 5. ผลลัพธ์ของ Sprint 1

* ได้โปรแกรมเครื่องคิดเลขที่สามารถทำงานได้จริง รองรับการบวก ลบ คูณ หาร
* มีการจัดการกรณีป้อนค่าที่ผิด เช่น การหารด้วยศูนย์
* รายงานความก้าวหน้าฉบับนี้เป็นผลสรุปการทำงานของ Sprint 1

---

# แผนการดำเนินงาน Sprint 2

* เพิ่มฟังก์ชันเพิ่มเติม เช่น ยกกำลัง หรือหารเอาเศษ
* พัฒนาให้โปรแกรมมีเมนูเลือกใช้งานที่สะดวกมากขึ้น
* ทดสอบและปรับปรุงต่อเนื่อง

---
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

---
# แผนการดำเนินงาน Sprint 3

## งานที่ต้องทำในสัปดาห์นี้
---

1. ตรวจสอบและปรับปรุงโค้ด
*	ตรวจสอบว่า simple_calculator() รองรับทุกฟังก์ชัน (binary/unary) ถูกต้อง
*	เพิ่ม try-except ในส่วน input เพื่อป้องกัน crash ถ้าผู้ใช้ป้อนตัวอักษร
*	ตรวจสอบการปัดทศนิยม (round()) ของแต่ละฟังก์ชัน
*	ตรวจสอบการจัดการ division by zero และ factorial ที่ผิดเงื่อนไข

2. ทำ Unit Test
*	ทดสอบฟังก์ชันแต่ละตัวแยกกัน: add, subtract, multiply, divide, sin, cos, tan, sqrt, pow2, fact
*	ทดสอบทั้ง input ปกติ และ input ผิด/edge cases

3. ทำ Integration Test
*	ทดสอบระบบทั้งหมดรวม main loop (calculator())
*	ตรวจสอบ input expression แบบต่าง ๆ
*	ตรวจสอบการป้อน exit และการแสดงผล separator / message

4. Debug และแก้ไขปัญหา
*	แก้ bug ที่พบจาก unit/integration test
*	ตรวจสอบข้อความ error ให้เข้าใจง่ายและตรงตามเงื่อนไข

## การแบ่งหน้าที่ในธีม
---
1. ชม (Planner & Debugger)
* วางแผนการทำงาน
* ออกแบบโครงสร้างเมนูโปรแกรม
* ตรวจสอบ logic ของฟังก์ชัน และช่วยแก้ไขข้อผิดพลาด (bugs)
* ออกแบบ UX และ flow การป้อน expression
2. ดิสก์ (Coder & Debugger)
* เขียนฟังก์ชันคำนวณ (simple_calculator) และ main loop (calculator)
* ทดสอบโปรแกรมเบื้องต้น ทำ unit test, integration test และแก้ไขบั๊กจากผลการทดสอบ


## อธิบายโค้ดที่เพิ่มเข้ามา
---
### 1. ฟังก์ชันคำนวณ simple_calculator(expr)
* Binary operator: +, -, *, /
*	รับ input 2 ตัวเลข เช่น "5 + 3"
*	ตรวจสอบ division by zero
*	ใช้ round(...,2) สำหรับ precision
*	Unary operator: sin, cos, tan, sqrt, pow2, fact เช่น "sin 90", "sqrt 16", "pow2 5", "fact 5"
*	sin, cos, tan ใช้ math.radians(a)
*	sqrt → sqrt ของตัวเลข
*	pow2 → ยกกำลัง 2
*	fact → factorial ของจำนวนเต็ม ≥ 0
*	Error handling:
*	ใช้ try-except เพื่อจับ error input ไม่ถูกต้องหรือ format ผิด
*	แสดงข้อความ error แทน crash โปรแกรม

### 2. Main Loop calculator()
* แสดง เมนูและตัวอย่างการป้อน expression
*	while True ให้ผู้ใช้ป้อน expression ต่อเนื่อง
*	ป้อน "exit" → โปรแกรมหยุดทำงาน
*	เรียก simple_calculator(expr) เพื่อคำนวณและแสดงผล
*	แสดง Result: พร้อม separator เพื่อความชัดเจน


## Test case
---

Enter expression: 10 + 1
  
  Result: 11.0

Enter expression: 10 - 8
  
  Result: 2.0

Enter expression: 15 + -3
  
  Result: 12.0

Enter expression: 6 * 3
  
  Result: 18.0

Enter expression: 8 / 4
  
  Result: 2.0

Enter expression: 8 / 0
  
  Result: Cannot divide by zero

Enter expression: sin 30
  
  Result: 0.5

Enter expression: cos 45
  
  Result: 0.7071

Enter expression: tan 45
  
  Result: 1.0

Enter expression: sin 31.5
  
  Result: 0.5225

Enter expression: sqrt 64
  
  Result: 8.0

Enter expression: sqrt 150
  
  Result: 12.25

Enter expression: pow2 67
  
  Result: 4489.0

Enter expression: pow2 10.5
  
  Result: 110.25

Enter expression: fact 10
  
  Result: 3628800

Enter expression: face -2
  
  Result: Unknown operator. Please try agian.

Enter expression: fact 0
  
  Result: 1

Enter expression: 5+3
  
  Result: Invalid input format

Enter expression: sin 30 + 5
  
  Result: Invalid input format

Enter expression: 4 + 2 * 5
  
  Result: Invalid input format

Enter expression: cos (30)
  
  Result: Error: could not convert string to float: '(30)'

Enter expression: tan 90
  
  Result: 1.633123935319537e+16


 ## Integration Test (ทดสอบระบบทั้งหมด)
 ---
	•	ป้อน binary expression → ตรวจสอบผลลัพธ์ถูกต้อง
	•	ป้อน unary expression → ตรวจสอบผลลัพธ์ถูกต้อง
	•	ป้อน input ไม่ถูกต้อง เช่น "abc + 5" → แสดง error message
	•	ป้อน operator ไม่รู้จัก → "Unknown operator. Please try again."
	•	ป้อน expression ผิด format เช่น "5 +" → "Invalid input format"
	•	ป้อน "exit" → โปรแกรมหยุดทำงาน


## error ที่พบเจอ
---
1.	ZeroDivisionError
* 	สาเหตุ: / กับตัวหาร = 0
* 	แก้ไข: if b == 0:   return "Cannot divide by zero"
2.	Input ไม่ใช่ตัวเลข
* 	สาเหตุ: float("abc") → ValueError
* 	แก้ไข: try-except เพื่อจับ error
3.	Factorial ไม่เป็นจำนวนเต็มหรือ <0
* 	ตรวจสอบ: a.is_integer() and a >= 0
* 	Error message: "Factorial must be greater than zero."
4.	Operator ไม่รู้จัก
*	 แสดงข้อความแจ้งผู้ใช้: "Unknown operator. Please try again."
5.	Expression format ผิด
* 	เช่น "5 +" → "Invalid input format"
6.	Rounding errors
* 	ใช้ round(...,2) สำหรับ binary operator
* 	ใช้ round(...,4) สำหรับ trig functions


