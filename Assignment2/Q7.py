# Find the factorial of a number using a while loop.

num = int(input("Enter a number for Factorial: "))
temp = num
factorial = 1
while temp > 0:
    factorial *= temp
    temp -= 1
print(f"The factorial of {num} is {factorial}")