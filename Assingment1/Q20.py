# Create a program that evaluates if an inputted number is prime.

num = int(input("Enter a number: "))
is_Prime = True
if num <= 0:
    is_Prime = False
elif num == 2:
    is_Prime = True
elif num % 2 == 0:
    is_Prime = False    
else:
    for i in range(3,int(num ** 0.5) +1, 2):
        if num % i == 0:
            is_Prime = False
            break
if is_Prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")