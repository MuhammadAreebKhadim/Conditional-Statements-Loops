# Write a program that checks if a given year is a leap year.

year = int(input("Enter year: "))
if year%4 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")