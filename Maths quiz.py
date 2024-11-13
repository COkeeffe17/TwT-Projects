# Maths quiz game, 10 questions, time how long to answer all of them. Wanted to assign num1 and num2 in the main loop and pass them in, 
# but if all operations used the same range pool multiplication questions wopuld be brutal, not to mention the looping in div would make it irrelevant for those questions.
# Tech with Tims was a lot smaller, but he used the same small range for all questions, and didnt do division.

import random, os, time



def add():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    answer = num1 + num2
    inp = "0"
    while inp != str(answer):
        inp = input(f"What is {num1} + {num2}?   ")


def sub():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    answer = num1 - num2 if num1 > num2 else num2 - num1
    message = f"What is {num1} - {num2}?   " if num1 > num2 else f"What is {num2} - {num1}?   "
    inp = "0"
    while inp != str(answer):
        inp = input(message)


def mult():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = num1 * num2
    inp = "0"
    while inp != str(answer):
        inp = input(f"What is {num1} * {num2}?   ")


def div():
    num1, num2 = 7, 2
    while num1 % num2 != 0 and num2 % num1 != 0:
        num1 = random.randint(1, 300)
        num2 = random.randint(1, 300)
    answer = num1 / num2 if num1 > num2 else num2 / num1 
    message = f"What is {num1} / {num2}?   " if num1 > num2 else f"What is {num2} / {num1}?   "
    inp = "0"
    while inp != str(answer):
        inp = input(message)


os.system('cls')
start = time.time()

for i in range(1, 11):
    operators = [add, sub, mult, div]
    operator = random.choice(operators)
    operator()
    os.system('cls')

end = time.time()
print(f"Time taken: {end - start} seconds.")
