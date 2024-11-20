# Password generator. Pretty simple, and I have had experience making this sort of thing before for my computer science NEA.

import string, random, os, pyperclip

# 0: String that will be used to generate the password  1: Uppercase   2: Numbers   3: Special
characters = [char for char in string.ascii_letters if char.islower()], [char for char in string.ascii_letters if not char.islower()], [char for char in string.digits], [char for char in string.punctuation]

choices = ["placeholder", "placeholder", "placeholder"]


# User choices
while choices[0].lower() != "n" and choices[0].lower() != "y":
    choices[0] = input("Would you like to have uppercase letters in your password (y/n)?   ")

while choices[1].lower() != "n" and choices[1].lower() != "y":
    choices[1] = input("Would you like to have numbers in your password (y/n)?   ")

while choices[2].lower() != "n" and choices[2].lower() != "y":
    choices[2] = input("Would you like to have special characters in your password (y/n)?   ")

length = "a"
while not length.isnumeric():
    length = input("How long would you like your password to be?   ")


# Which characters being used
for i in range(0, 3):
    if choices[i].lower() == "y":
        for char in characters[i+1]:
            characters[0].append(char)

# Random password generation
password = []
for i in range(0, int(length)):
    password.append(characters[0][random.randint(0, len(characters[0])-1)])

os.system('cls')
print("Your new password is:", "".join(password))


# Unnecessary but nonetheless useful copying
copy = input("Would you like to copy this to clipboard?   ")

if copy.lower() in ["yes", "y"]:
    pyperclip.copy("".join(password))
