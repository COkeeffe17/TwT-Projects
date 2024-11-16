# Multiplayer game in which players take turns rolling a dice repeatedly, risking their score if they roll a 1. First to 50 wins. 2-4 players (as more would be way too long of a game).

import random, time, os


def checkwin(players):
    # If any players have reached the winning score of 50 points yet
    for player in players:
        if player[1] >= 50:
            os.system('cls')
            print(f"{player[0]} is the winner, with {player[1]} points!") 
            time.sleep(5)
            return True
    return False


def printscores(players):
    # Prints scores. Thats it.
    for player in players:
        print(f"{player[0]}: {player[1]}")
    print('\n' * 3)


def main():
    howmany = "9"

    # How many players
    while not howmany.isdigit() or not (1 < int(howmany) < 5):
        howmany = input("How many players will play today (2-4)?   ")

    os.system('cls')

    players = []
    for i in range(0, int(howmany)):
        players.append([f"Player {i+1}", 0])

    over = False
    num = 0
    while not over:
            # Basically controls whos turn it is to play using the ever increasing "num" variable
            try:
                player = players[num]
            except:
                num = 0
                player = players[num]

            taken = False
            temp = 0

            # Loops until the player takes their score, or it is taken from them
            while not taken:
                choice = ""
                os.system('cls')
                printscores(players)
                print(f"{player[0]}'s turn:\n")
                print(f"This round's score: {temp}\n")
                
                while choice != "r" and choice != "t":
                    choice = input("Would you like to roll the dice, or take your current score (r/t)?   ")

                # Take
                if choice.lower() == "t":
                    players[num][1] == temp 
                    taken = True
                    print(f"{player[0]} gained {temp} points.")
                    players[num][1] += temp
                    time.sleep(1.5)

                # Roll            
                else:
                    roll = random.randint(1, 6)
                    print(f"{player[0]} rolled a {roll}.")
                    if roll == 1:
                        temp = 0
                        print(f"Uh oh, {player[0]} lost everything from this round!")
                        time.sleep(2)
                        taken = True
                    
                    else:
                        temp += roll
                        time.sleep(1.5)
                
                over = checkwin(players)
            num += 1             


main()
