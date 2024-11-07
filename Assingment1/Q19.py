# Check if a string input is uppercase, lowercase, or a mix.


text = input("Enter a string: ")

if text.isupper():
    print("The string is in uppercase.")
elif text.islower():
    print("The string is in lowercase.")
else:
    print("The string is a mix of uppercase and lowercase.")
