number = 10
print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q':
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = int(input("Sorry, that's not correct. Try again? "))
print(f"The number was {number}. Goodbye!")