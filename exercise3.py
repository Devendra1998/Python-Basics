n=17
#no of guesses
#print no of guesses left
#game over
#no of guesses he took to finish the game
print("you have only 10 number of gusses")
print("Enter a number")
num=int(input())
if num==n:
     print("congratulate you have entered correct number")
elif num>n:
    print("you enter greater number")
else:
    print("you enter smaller number ")
    print("no of gusses left")