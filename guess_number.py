number = 10
print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q':
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        if guess < number:
            print("Sorry! Your guess was too low.")
        else:
            print("Sorry! Your guess was too high.")

        guess = int(input("Try again? "))

print(f"The number was {number}. Goodbye!")