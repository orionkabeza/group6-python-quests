def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide a number by zero."
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ")

if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1,num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation, let's try something else."

print("Result: ", result)
