#Snake water gun

import random
score=0
choice = random.choice(["snake","water","Gun"])
chaances=10
a=input("s for snake, g for gun,w for water")

while(chaances!=1):
    if (choice == "snake" and a == "snake"):
        print("you are tied with computer and score", score)
    elif (choice == "snake" and a == "water"):
        score = score - 1
        print("computer wins and score", score)
    elif (choice == "snake" and a == "Gun"):
        score = score + 1
        print("You win and score", score)
    elif (choice == "water" and a == "snake"):
        score = score + 1
        print("you win and score", score)
    elif (choice == "water" and a == "water"):

        print("you tied with computer and score", score)
    elif (choice == "water" and a == "Gun"):
        score = score - 1
        print("Computer win and score", score)
    elif (choice == "Gun" and a == "snake"):
        score = score - 1
        print("computer win and score", score)
    elif (choice == "Gun" and a == "Gun"):
        print("you tied with computer and score ", score)
    elif (choice == "Gun" and a == "water"):
        score = score + 1
        print("You win and score", ++score)
    chaances=chaances-1




