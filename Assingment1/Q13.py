# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = input("Enter operation (+, -, *, /): ")


if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print("Invalid operation")
