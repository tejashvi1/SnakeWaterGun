import random

def game():
    pass

randomno = random.randint(1,3)

if randomno == 1:
    comp = 'S'
    print("Computer Selected Snake")
elif randomno == 2:
    comp = 'W'
    print("Computer Selected Water")

elif randomno == 3:
    comp = 'G'
    print("Computer Selected Gun")

p2 =  input("Player's Turn Snake(S) Water(W) Gun(G) ?")


if(comp == "S" and p2 == "G" or comp == 'S' and p2 == "W"):
    print("Player Win")
elif(comp == "W" and p2 == "G" or comp == 'W' and p2 == "S"):
    print("Computer Win")
else:
    print("Game Ties")

