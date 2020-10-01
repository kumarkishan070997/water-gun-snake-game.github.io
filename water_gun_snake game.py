#Please welcome us yar..
print("Welcome to Python Game : Snake,Water,Gun game..")
#give your name proof that you have created it by..
print("Coded by Kumarkrishna070997")
import random
count=0
userc=0
cmpc=0
total=10
i=1
list=["s","w","g"]
cmp=random.choice(list);
list2=["s","g","w"]
while i<=total:
    user = input("Enter your choice: ")
    if user in list2:
            if user==cmp:
                print("You both choose the same thing\nsystem:",cmpc,"\tuser:",userc,"\t attempts left:",total-i)
            elif cmp=="s" and user=="w":
                cmpc+=1
                print("System wins this time...\nsystem:",cmpc,"\tuser",userc,"\t attempts left:",total-i)
            elif cmp=="w" and user=="s":
                userc+=1
                print("You wins this time...\nsystem:",cmpc,"\tuser",userc,"\t attempts left:",total-i)
            elif cmp=="s" and user=="g":
                userc+=1
                print("You wins this time...\nsystem:",cmpc,"\tuser",userc,"\t attempts left:",total-i)
            elif cmp=="g" and user=="s":
                cmpc+=1
                print("System wins this time...\nsystem:",cmpc,"\tuser",userc,"\t attempts left:",total-i)
            elif cmp=="g" and user=="w":
                userc+=1
                print("You wins this time...\nsystem:",cmpc,"\tuser",userc,"\t attempts left:",total-i)
            else:
                cmpc+=1
                print("System wins this time...\nsystem:",cmpc,"\tuser",userc,"\t attempts left:",total-i)
    i+=1

while i>=total+1:
    print("GAME OVER!!!")
    if cmpc>userc:
        print("System:",cmpc,"\tUser:",userc,"\nYou lose the game..")
        break
    elif cmpc<userc:
        print("System:",cmpc,"\tUser:",userc,"\n Yeah.. You WIN the game..")
        break
    else:
        print("System:",cmpc,"\tUser:",userc,"\nDRAW..")
        break

