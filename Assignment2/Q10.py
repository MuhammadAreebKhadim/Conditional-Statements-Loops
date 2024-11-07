#  Use a loop to count the number of digits in an integer.

num = int(input("Enter the number of digits: "))
count = 0 
while num > 0: 
    num //= 10
    count += 1 
print(f"The number has {count} digits")
