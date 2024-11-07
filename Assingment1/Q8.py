# Create a program that checks if a given string is a palindrome.


string = input("Enter a string: ")
cleaned_string = string.replace(" ","").lower()
if cleaned_string == cleaned_string[::-1]:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
