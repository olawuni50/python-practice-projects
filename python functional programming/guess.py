"""
a) Let the computer pick a random number between 0 and 111( including both).
b) Let the user enter a guess for the number, if correct, print eh number of guesses that were
needed. it not, tell the user fi the number is higher or lower, and let the user guess again (and so on).
c) if the user enters "quit" or "q" instead of a number, quit the game.
"""

import random
exit = "q"
exited = "quit"

secretNumber = random.randint(0, 111) #random number from 0 - 111

f = 0
while True:
    val = input("please enter a number: ")
    f += 1
    if val == exit or val == exited:
        print("you have successfully exited the game")
        break
    try:
        if int(val) == secretNumber:
            print("you guess {} time(s) before you guessed right".format(f))
            break
    except ValueError:
        continue
