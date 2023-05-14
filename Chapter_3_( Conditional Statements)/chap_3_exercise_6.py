# Number guessing game:
import random

winning_num= random.randint(1,100)
print("Enter a number between 1 to 100: ")

i=0

while True:
    guessing_num=int(input())
    i+=1
    if guessing_num>winning_num:
        print("Too High")
        print("Guess again: ")
        continue

    elif guessing_num<winning_num:
        print("Too Low")
        print("Guess again: ")
        continue
    elif guessing_num==winning_num:
        print(f"You win after trying {i} times")
        break



