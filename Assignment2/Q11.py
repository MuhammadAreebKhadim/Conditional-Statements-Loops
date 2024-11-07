# Print the reverse of a given number.


num = int(input("Enter a number: "))
reverse_num = 0

while num > 0:
    remainder = num % 10
    reverse_num = (reverse_num * 10) + remainder
    num //= 10

print(f"Reversed number is {reverse_num}")
