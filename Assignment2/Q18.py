# Use a loop to print numbers in reverse order within a given range.

start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
for i in range(start, end - 1, -1):
    print(i)