# DRY - don't repeat yourself
# Number guessing game:
import random
win_num= random.randint(1,100)
guess=1
num=int(input("guess a number between 1 and 100: "))
game_over= False

while not game_over:
    if num==win_num:
        print(f"you win, and you guessed this number in {guess} times")
        game_over= True
    else:
        if num<win_num:
            print("too Low")
        else:
            print("too High")
        
        guess+=1
        num=int(input("guess again: "))
