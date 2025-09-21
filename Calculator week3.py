import math

def simple_calculator(expr):
    tokens = expr.split()

    try:
        # กรณีเป็น binary operator (+ - * /)
        if len(tokens) == 3:
            a, operator, b = tokens
            a = float(a)
            b = float(b)

            if operator == "+":
                return round(a + b, 2)
            elif operator == "-":
                return round(a - b, 2)
            elif operator == "*":
                return round(a * b, 2)
            elif operator == "/":
                if b == 0:
                    return "Cannot divide by zero"
                return round(a / b, 2)
            else:
                return "Unknown operator. Please try again."

        # กรณีเป็น unary operator (sin, cos, tan, sqrt, pow2, factorial)
        elif len(tokens) == 2:
            operator, a = tokens
            a = float(a)

            if operator == "sin":
                return round(math.sin(math.radians(a)), 4)
            elif operator == "cos":
                return round(math.cos(math.radians(a)), 4)
            elif operator == "tan":
                return round(math.tan(math.radians(a)), 4)
            elif operator == "sqrt":
                return round(math.sqrt(a), 2)
            elif operator == "pow2":
                return round(math.pow(a, 2), 2)
            elif operator == "fact":
                if a.is_integer() and a >= 0:
                    return math.factorial(int(a))
                else:
                    return "Factorial must be greater than zero."
            else:
                return "Unknown operator. Please try agian."

        else:
            return "Invalid input format"

    except Exception as e:
        return f"Error: {e}"

# main loop
def calculator():
    print("=" * 35)
    print("       Simple Sci Calculator")
    print("=" * 35)
    print("Supported operations:")
    print("  + :  a + b ")
    print("  * :  a * b ")
    print("  - :  a - b")
    print("  / :  a / b")
    print("  sin x   |  cos x   |  tan x")
    print("  sqrt x  |  pow2 x  |  fact n")
    print("-" * 35)
    #print("Type 'exit' to quit.\n")

    while True:
        expr = input("Enter expression: ")
        if expr.lower() == "exit":
            print("\n" + "=" * 35)
            print("      End of Program")
            print("=" * 35)
            break
        result = simple_calculator(expr)
        print("Result:", result)
        print("-" * 35)


calculator()
