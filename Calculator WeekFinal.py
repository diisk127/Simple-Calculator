import tkinter as tk
import math

# ---------------- Logic ----------------
def simple_calculator(expr):
    tokens = expr.split()

    try:
        if len(tokens) == 3:  # binary operator
            a, operator, b = tokens
            a = float(a)
            b = float(b)

            if operator == "+":
                return round(a + b, 4)
            elif operator == "-":
                return round(a - b, 4)
            elif operator == "×":
                return round(a * b, 4)
            elif operator == "÷":
                if b == 0:
                    return "Error"
                return round(a / b, 4)
            else:
                return "Unknown operator"

        elif len(tokens) == 2:  # unary operator
            a, operator = tokens
            a = float(a)

            if operator == "sin":
                return round(math.sin(math.radians(a)), 4)
            elif operator == "cos":
                return round(math.cos(math.radians(a)), 4)
            elif operator == "tan":
                return round(math.tan(math.radians(a)), 4)
            elif operator == "²√x":
                return round(math.sqrt(a), 4)
            elif operator == "x²":
                return round(math.pow(a, 2), 4)
            elif operator == "fact":
                if a < 0 or not a.is_integer():
                    return "Error"
                return math.factorial(int(a))
            else:
                return "Unknown operator"

        else:
            return "Invalid input format"

    except Exception:
        return "Error"


# ---------------- GUI ----------------
button_values = [
    ["AC", "⌫", "²√x", "x²", "÷"],
    ["sin", "7", "8", "9", "×"],
    ["cos", "4", "5", "6", "-"],
    ["tan", "1", "2", "3", "+"],
    ["fact", "00", "0", ".", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "⌫"]
trig_functions = ["sin", "cos", "tan"]
special_functions = ["²√x", "x²", "fact"]

color_medium_gray = "#A0A0A0"
color_black = "#1C1C1C"
color_orange = "#FF9500"

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
window.configure(bg=color_black)

frame = tk.Frame(window, bg=color_black)

# แถวบนสำหรับโชว์ expression
expr_label = tk.Label(frame, text="", font=("Arial", 20), background=color_black,
                      foreground="white", anchor="e", width=12, height=1)
expr_label.grid(row=0, column=0, columnspan=5, sticky="we", padx=5, pady=2)

# แถวล่างสำหรับโชว์ผลลัพธ์
label = tk.Label(frame, text="0", font=("Arial", 40), background=color_black,
                 foreground=color_orange, anchor="e", width=12, height=2)
label.grid(row=1, column=0, columnspan=5, sticky="we", padx=5, pady=2)

# ---------------- Functions ----------------
A = None
operator = None

def clear_all():
    global A, operator
    label["text"] = "0"
    expr_label["text"] = ""
    A = None
    operator = None

def backspace():
    current = label["text"]
    if len(current) > 1:
        label["text"] = current[:-1]
    else:
        label["text"] = "0"

def button_clicked(value):
    global A, operator
    current = label["text"]

    if value == "AC":
        clear_all()

    elif value == "⌫":
        backspace()

    elif value in right_symbols:  # + - × ÷ =
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                expr = f"{A} {operator} {B}"
                result = simple_calculator(expr)

                # แสดง expression + result บน GUI
                expr_label["text"] = expr + " ="
                label["text"] = str(result)

                A = None
                operator = None
        else:  # set operator
            A = label["text"]
            operator = value
            expr_label["text"] = f"{A} {operator}"
            label["text"] = "0"

    elif value in  special_functions + trig_functions:
        num = float(label["text"])
        result = simple_calculator(f"{num} {value}")
        expr_label["text"] = f"{value}({num})"
        label["text"] = str(result)

    else:  # digits or .
        if current == "0":
            label["text"] = value
        else:
            label["text"] += value


# ---------------- Create Buttons ----------------
for r, row in enumerate(button_values):
    for c, val in enumerate(row):
        btn = tk.Button(frame, text=val, font=("Arial", 20),
                        width=4, height=2,
                        command=lambda v=val: button_clicked(v))

        if val in top_symbols or val in right_symbols or val in trig_functions or val in special_functions:
            btn.config(foreground=color_black, background=color_medium_gray)
        else:
            btn.config(foreground=color_black, background=color_medium_gray)

        btn.grid(row=r+2, column=c, padx=2, pady=2, sticky="nsew")

for i in range(5):
    frame.columnconfigure(i, weight=1)
for i in range(len(button_values)+2):
    frame.rowconfigure(i, weight=1)

frame.pack(padx=10, pady=10)

window.mainloop()
