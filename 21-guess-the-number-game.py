# A game for gussing numbers , if you matched the randomly generated number , 
# you win , if you failed , the game will terminate after the 6th attempt 

import random

playerName = input("What's your name ?\t")
print(f"Well , {playerName} , i'm thinking of a number between 1 and 10")
print("you have 6 attempts of trial and error!\n\n")

def numberCheck(playerNumber):
    randomNumber = random.randint(1,3)
    if int(playerNumber) == randomNumber:
        print("you're right")
        return(True)
    elif (int(playerNumber) - randomNumber) < 3 :
        print("you're Wrong , yet close ...")
    else:
        print(f"The number {playerNumber} , doesn't match {randomNumber} ")
        return(False)

i = 0
while i < 6 :
    playerNumber = input(f"Take a guess \t")
    if numberCheck(playerNumber) == True :
        print(f"You won the game {playerName} , you've guessed the number in {i+1} guesses")
        break
    i+= 1
