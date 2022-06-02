import random

guessedNum = random.randint(0, 40)
count = 0
while count < 5:
    guess = int(input("guess a number between (0-30): "))
    if guess < guessedNum:
        print("too low")
    elif guess > guessedNum:
        print("too high")
    else:
        print("awesome, you're correct")
        break
    count += 1

else:
    print("you tired, but you can never make it!")


