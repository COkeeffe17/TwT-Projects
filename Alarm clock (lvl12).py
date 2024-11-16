# Alarm clock. Pretty easy, tried using his CLEAR and CLEAR_AND_RETURN constants, but os.system('cls') works much better for me. He did it by only counting seconds and converting that to minutes, 
# but i counted both minutes and seconds. In the end they result in about the same number of lines, mine is just longer for looping and input validation.

import time, os
from playsound import playsound


def alarm(minutes, seconds):
    while seconds != 0 or minutes != 0:

        seconds -= 1

        os.system('cls')
        print("Time left: " + str(minutes if minutes >= 10 else "0" + str(minutes)) + ":" + str(seconds if seconds >= 10 else "0" + str(seconds)))
        time.sleep(1)

        if seconds == 0 and minutes != 0:
            minutes -= 1
            seconds = 59  


    playsound("Alarm_sound.mp3")


again = "y"

while again != "n":
    minutes, seconds = "a", "a"

    while not minutes.isdigit():
        minutes = input("How many minutes should this alarm go for?   ")

    while not seconds.isdigit() or not (0 <= int(seconds) <= 59):
        seconds = input("How many seconds should this alarm go for?   ")


    alarm(int(minutes), int(seconds) + 1)

    again = "a"

    while again != "y" and again != "n":
        os.system('cls')
        again = input("Would you like to go again?   ")
