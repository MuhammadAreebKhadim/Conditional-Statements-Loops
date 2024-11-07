# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The sides do not form a valid triangle.")
