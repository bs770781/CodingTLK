import random

# Generate a random number between 1 trough 10
random_number = random.randint(1, 10)

# User Should guess
guess = None

# Keep asking the user to guess until they guess correctly
while guess != random_number:
    guess = int(input("Guess the number: "))

    if guess != random_number:
        print("Wrong, try again!")
    else:
        print("Correct! 🎉")
#Code Goes on until user gets it right