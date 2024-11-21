# Mastermind game. Pretty easy, not sure why it says advanced, the only sticky part was the "wrong position" characters. I did it completely independently, but after watching his back I did like his use of the zip() function, so I took that.
# I also think that the way he handled the "wrong position" characters was better than mine, but I think mine works after some play-testing, so I didn't change it.

import os, random

def suffix(guess):
    # I hate janky messages, so here we are
    if guess == 1:
        return "st"
    elif guess == 2:
        return "nd"
    elif guess == 3:
        return "rd"
    else:
        return "th"


def checkplaces(guess, answer):
    correct, almost = 0, 0
    # Getting how many characters are correct, and how many need to be moved.
    for g, r in zip(guess, answer):
        if r == g:
            correct += 1           
        elif r in guess:
            if answer.count(r) <= guess.count(r):
                almost += 1
    
    return correct, almost


COLOURS = ["R", "O", "Y", "G", "B", "P"]

over = False

# Messages
os.system('cls')
print("Welcome to Mastermind. You get 10 attempts to guess a 4 digit code comprised of these letters, representing colours:\n")
print(COLOURS, "\n")


# Making the answer
answer = []
for i in range(0, 4):
    answer.append(COLOURS[random.randint(0, 5)])

attempt = 0

while not over and attempt < 10:
    attempt += 1
    guess = "11111"

    # Input
    while len(guess) != 4 or not guess.isalpha():
        guess = input(f"Enter your {attempt}{suffix(attempt)} guess:   ")


    guess = list(guess)

    # I'm not dealing with caps vs no caps
    for i in range(0, 4):
        guess[i] = guess[i].upper()

    correct, almost = checkplaces(guess, answer)

    print(f"Correct position: {correct} | Incorrect position: {almost}")

    if correct == 4:
        over = True

if guess == answer:
    print(f"\nYou got it on your {attempt}{suffix(attempt)} guess!")

else:
    "".join(answer)
    print(f"Unlucky, the answer was {answer}")
