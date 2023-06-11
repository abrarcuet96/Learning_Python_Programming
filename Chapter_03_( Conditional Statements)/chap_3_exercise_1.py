# Exercise_01: Number guessing game.

# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# If user guessed correctly then print "YOU WIN!!".
# If user didn't guessed correctly then:
# --> if user guessed lower than actual number then print "too low".
# --> if user guessed higher than actual number then print "too high".

# Bonus:
# Google "How to generate random number in python" to generate random winning number.

import random

# Nested if_else:
# Simple Method:
winning_num= 96
guessing_num= int(input("Guess the number between 1 to 100: "))

if winning_num==guessing_num:
    print("YOU WINN!!")
else:
    if guessing_num<winning_num:
        print("Too Low")
    else:
        print("Too High")


# Using random function:
winning_num= random.randint(0,100)
guessing_num= int(input("Guess the number between 1 to 100: "))

if winning_num==guessing_num:
    print("YOU WINN!!")
else:
    if guessing_num<winning_num:
        print("Too Low")
    else:
        print("Too High")