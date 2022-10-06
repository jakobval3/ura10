import random

secret = random.randint(1, 30)
attempts = 0

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {guess}" )
        print(f"Attempts needed: {attempts}")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")