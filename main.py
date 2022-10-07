import random


secret = random.randint(1, 30)
attempts= 0
best_score= None
print(secret)



with open("score.txt", "r") as file:
    best_score= int(file.read())
    print(f"Top score: {best_score}")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {guess}" )
        print(f"Attempts needed: {attempts}")
        if  best_score > attempts:
            with open("score.txt", "w") as file:
                file.write(str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")