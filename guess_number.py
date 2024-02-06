number = 10
num_guesses = 5
print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q' and num_guesses > 0:
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        num_guesses -= 1
        guess = int(input(f"Sorry, that's not correct. You have {num_guesses} guesses left. Try again? "))
print(f"The number was {number}. Goodbye!")