# Simple Calculator:

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y

def power(x,y):
    return x**y

print("Calculator Operations: +, -, *, /, **")
num1=float(input("Enter the first number: "))
op=input("Enter the operator +, -, *, / or **: ")
num2=float(input("Enter the second number: "))

if op == "+":
    print("Result: ", add(num1,num2))
elif op == "-":
    print("Result: ", subtract(num1,num2))
elif op == "*":
    print("Result: ", multiply(num1,num2))
elif op=="/":
    if num2==0:
        print("Error: Division by zero")
    else:
        print("Result: ", divide(num1,num2))
elif op=="**":
    print("Result: ", power(num1,num2))
else:
    print("Invalid operation")
    
        
    
    

    
