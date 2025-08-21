# ฟังก์ชันการบวก
def add(a,b):
  return round(a + b, 2)

# ฟังก์ชันการลบ
def subtract(a,b):
  return round(a - b, 2)

# ฟังก์ชันการคูณ
def multiply(a,b):
  return round(a * b,2)

# ฟังก์ชันการหาร
def divide(a,b):
  # ถ้าตัวหาร (b) = 0
  if b == 0:
    return "Cannot divide by zero"
  return round(a / b, 2)

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
