import random

# computer_guess is a random number from 1 to 100
computer_guess = random.randint(1, 100)

user_guess = None

while user_guess != computer_guess:
    user_guess = input("Guess a number between 1 and 100: ")

    if not user_guess.isdigit():
        print("Sorry! cannot process that, enter a number")
        continue

    if int(user_guess) < computer_guess:
        print("Too low, try again!")
    elif int(user_guess) > computer_guess:
        print("Too high, try again!")
    else:
        print("  You got it! the number I guess was", computer_guess)
        break
