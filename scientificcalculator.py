
import math

op   = input("Enter the operator: ")
num1 = float(input("Enter the first number: "))





if op == '+':
    num2 = float(input("Enter the second number: "))
    print(num1 + num2)
    
if op == '-':
    num2 = float(input("Enter the second number: "))
    print(num1 - num2)
    
if op == '*':
    num2 = float(input("Enter the second number: "))
    print(num1 * num2)
    
if op == '/':
    num2 = float(input("Enter the second number: "))
    print(num1 / num2)

if op == 'sin':
    print(math.sin(num1))

elif op == 'cos':
    print(math.cos(num1))

elif op == 'tan':
    print(math.tan(num1))

elif op == 'sqrt':
    print(math.sqrt(num1))

elif op == 'floor':
    print(math.floor(num1))

elif op == 'ceil':
    print(math.ceil(num1))



else:
    print("Invalid operator")
    