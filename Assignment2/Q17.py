# Write a program that continues to ask for a number until the correct number is guessed.

correct_num = 7  
while True:
    guess = int(input("Guess the number: "))
    if guess == correct_num:
        print("You guessed it right!")
        break
    print("Try again.")