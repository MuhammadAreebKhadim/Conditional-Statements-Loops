# Write a program that breaks the loop when a certain condition is met.

for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print(i)
