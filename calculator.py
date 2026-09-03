# BTech CSE First Year
print("=== Simple Calculator ===")

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Answer =", a + b)
elif op == "-":
    print("Answer =", a - b)
elif op == "*":
    print("Answer =", a * b)
elif op == "/":
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
