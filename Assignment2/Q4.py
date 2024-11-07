# Print the multiplication table of a given number.

tab = int(input(" Enter a Number: "))
num = 1
for i in range(10):
    print(f"{tab} x {num} = {tab * num}")
    num += 1

# tab = int(input(" Enter a Number: "))
# num = 1
# while num <= 10:
#     print(f"{tab} x {num} = {tab * num}")
#     num += 1