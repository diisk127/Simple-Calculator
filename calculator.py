# ฟังก์ชันการบวก
def add(a, b):
    pass  

# ฟังก์ชันการลบ
def subtract(a, b):
    pass

# ฟังก์ชันการคูณ
def multiply(a, b):
    pass

# ฟังก์ชันการหาร
def divide(a, b):
    pass

# main function
def calculator():
    while True:
        print("-------- Calculator Menu --------")
        print("1. Add Function")
        print("2. Subtract Function")
        print("3. Multiply Function")
        print("4. Divide Function")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("End of the program...")
            break

        # รับค่าตัวเลขจากผู้ใช้
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        # เรียกใช้ฟังก์ชันตามตัวเลือก
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Invalid choice.")

# เรียกใช้งาน main function
calculator()

