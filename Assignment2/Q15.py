# Print the sum of even and odd numbers separately up to a given number.


n = int(input("Enter a number: "))
sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")
