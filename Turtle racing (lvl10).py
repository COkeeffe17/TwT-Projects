# Simple turtle racing game. Window is rescaleable and the racing will work, but not recommended as the speed of the turtles only changes with the number of turtles, not the size of the screen. 
# Also looks slightly wierder when zoomed out, but the functionality all works nonetheless. 

import turtle, random, os
 

howmany = "0"
# How many racers
while not howmany.isdigit() or not (1 < int(howmany) < 11):
    howmany = input("How many turtles would you like to race(2-10)?   ")

# Screen stuff
sc = turtle.Screen()
HEIGHT, WIDTH = 400, 300
sc.setup(HEIGHT, WIDTH)
sc.bgcolor("lightBlue")
sc.title("Turtle racing")

# Finish line
endline = turtle.Turtle(shape='turtle')
endline.speed(speed=0)
endline.penup()                   
endline.goto(-(WIDTH // 2), ((HEIGHT // 2) - 50))             
endline.pendown()
endline.pensize(10)
endline.goto((WIDTH // 2), ((HEIGHT // 2) - 50))

# Start line
startline = turtle.Turtle(shape='turtle')
startline.speed(speed=0)
startline.penup()                   
startline.goto(-(WIDTH // 2), (-(HEIGHT // 2) + 50))             
startline.pendown()
startline.pensize(10)
startline.goto((WIDTH // 2), (-(HEIGHT // 2) + 50))

turtles = []
spacing = ((WIDTH - int(howmany)) // (int(howmany) + 1))
basex = -(WIDTH // 2) + spacing
taken = []
colours = ["red", "blue", "green", "yellow", "black", "purple", "pink", "brown", "orange", "gray"]

def colourgenerator(taken, colours):
    # Gets a random colour from colours
    good = False
    while not good:
        colour = colours[random.randint(0, 9)]
        if colour not in taken:
            taken.append(colour)
            good = True

    return colour, taken


# Turtle generation loop
for i in range(0, int(howmany)):
    t = turtle.Turtle(shape='turtle')
    colour, taken = colourgenerator(taken, colours)
    t.color(colour)
    t.penup()                   
    t.goto(basex, (-(HEIGHT // 2) + 28))  
    t.left(90)
    t.pendown()
    turtles.append(t)
    basex += spacing

over = False
# Game loop
while not over:
    for t in turtles:
        move = random.randint(1, 3)
        if move == 1:
            t.forward(int(howmany))

    # Checkwin
    for t in turtles:
        if (t.pos())[1] >= ((HEIGHT // 2) - 50):
            over = True
            os.system('cls')
            print(f"Winner is the {t.pencolor()} turtle!")


turtle.done()
