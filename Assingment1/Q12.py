# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temp = int(input("Enter Temperature in Celsius: " ))
if temp <= 0:
    print(temp,"is freezing point")
elif temp >= 1 and temp <= 37:
    print(temp,"is moderate ")
else:
    print(temp,"is hot")

