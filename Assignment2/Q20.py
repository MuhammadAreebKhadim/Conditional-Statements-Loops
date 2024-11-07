# Create a program that simulates a countdown timer starting from a given number down to zero.

import time

num = int(input("Number: "))
while num >= 0:
    print(num)
    time.sleep(1)
    num -= 1
print("Time's up!")