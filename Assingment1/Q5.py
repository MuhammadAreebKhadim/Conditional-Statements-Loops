# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

num = int(input("Enter your number: "))

if num >= 90:
    print("Your grade is A")
elif num >=80:
    print("Your grade is B")
elif num >= 70:
    print("Your grade is C")
elif num >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")
