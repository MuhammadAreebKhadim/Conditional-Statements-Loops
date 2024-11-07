
# Create a program to calculate the sum of the digits of an inputted integer.

num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print(f"Sum of the digits: {sum_digits}")