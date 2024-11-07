#  Write a program to print the first 10 Fibonacci numbers.

n1 = 0 
n2 = 1
count = 0

while count < 10:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
    
num = int(input("Enter a Fibonacci number: "))
n1  = 0
n2 = 1
count = 0
while count < num:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1