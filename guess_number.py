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
        if guess < number:
            print("Sorry! Your guess was too low.")
        else:
            print("Sorry! Your guess was too high.")

        guess = int(input("You have {num_guesses} guesses left. Try again? "))

print(f"The number was {number}. Goodbye!")