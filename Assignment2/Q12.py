# Print all prime numbers between 1 and 50.

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# num = int(input("Enter a Number: "))
# for i in range(2,num+1):
#     is_prime = True
#     for j in range(2, int(num ** 0.5) + 1):   # use for square root ( ** )
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)
