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

p2 =  input("Player's Turn Snake(1) Water(2) Gun(3) ?")


if(comp != p2):
    print("Player Win")
else:
    print("Computer Win")

