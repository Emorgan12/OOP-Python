num1 = int(input("Enter num1: "))
op = input("Enter Operator: ")
num2 = int(input("Enter num2: "))

if op == "+":
     print(num1 + num2)
elif op == "-":
     print(num1 - num2)
elif op == "/":
     print(num1 / num2)
elif op == "*":
     print(num1 * num2)
else:
     print("Invalid Operator")