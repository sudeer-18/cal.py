a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
op=input("Enter the operator (+, -, *, / or %): ")
if op == "+":
    result = a+b
elif op == "-":
    result = a-b
elif op == "*":
    result = a*b
elif op == "/":
    if b != 0:
        result = a/b
    else:
        result = "Error: Division by zero"
elif op == "%":
    if b != 0:
        result = a%b
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
print("Result:", result)
