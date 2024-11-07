# Write a program to determine if a given character is a vowel or consonant.

char = input("Enter an Alphabet character: ")
vowel = ("a,e,i,o,u")
if char in vowel:
    print( char,"is a vowel.")
else:
    print(char, "is a consonant.")