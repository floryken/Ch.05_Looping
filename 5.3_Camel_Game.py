'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
done=False
nati=-20
thirst=0
miles=0
tired=0
canteen=6
dir=input("Would you like directions?\nY or N")
if dir.lower()=="y":
    print("Welcome to Bull Rider!")
    print("The goal of this game is to make it 200 miles across the field being chased by poachers")
    print("Every Once in a while you will be asked to give a choice\n\n\n")
    print("Your options will be")
    print(" 1. Drink from Your Bottle of Water\n 2. Forward at normal speed\n 3. Forward at Full Speed")
    print("4. Stop for night\n 5. Check Stats\n 6. Quit")
    print("Make sure to answer with the #!\nThe game is starting now...\n\n\n\n")
else:
    print("Game starting now...\n\n\n\n")
while not done:
    if nati<miles:
        if thirst<6 or tired<8:
            oasis=random.randint(1,20)
            if oasis==7:
                print("You found an oasis, You are rested and not thirsty")
                tired=0
                canteen=6
                thirst=0
            if nati>miles-15 and nati<miles:
                print("Poachers are close!\nThey are",miles-nati,"Behind you!")
            if tired>=5 and tired<=8:
                print("You are tired")
            if thirst>=4 and thirst<6:
                print("You are thirsty")
            if miles<200:
                print("What would you like to do?")
                user_choice=int(input(" 1. Drink from Your Bottle of Water\n 2. Forward at normal speed\n 3. Forward at Full Speed\n 4. Stop for night\n 5. Check Stats\n 6. Quit"))
                if user_choice==6:
                    done=True
                    break
                elif user_choice==5:
                    print("Here are your stats:")
                    print("Miles Traveled:",miles,"\nCanteen Uses Left:",canteen,"\nDistance from poachers:",miles-nati)
                elif user_choice==4:
                    print("You Rest for the Night.")
                    tired=0
                    nati+=random.randint(7,14)
                elif user_choice==3:
                    spe=random.randint(10,20)
                    print("You Move Forward:",spe)
                    miles+=spe
                    thirst+=1
                    tired+=random.randint(1,3)
                    nati += random.randint(7, 14)
                elif user_choice==2:
                    spe=random.randint(5,12)
                    print("You move Forward:",spe)
                    miles+=spe
                    thirst+=1
                    tired+=1
                    nati += random.randint(7, 14)
                elif user_choice==1:
                    if canteen>=1:
                        canteen -= 1
                        print("You take a Drink and feel refreshed! You have", canteen, "Uses left.")
                        thirst=0
                    else:
                        print("OOF you done ran out of water! Best not die")
                else:
                    print("Pick an actual # please!")
            else:
                print("You won!!")
                again = input("Would you like to play again?  Y/N")
                if again.lower() == "y":
                    nati = -20
                    thirst = 0
                    miles = 0
                    tired = 0
                    canteen = 6
                    continue
                elif again.lower() == "n":
                    done == True
                    break
                else:
                    print("Not an Option")
        else:
            print("Your Bull died\nYou made it:",miles,"Miles")
            again = input("Would you like to play again?  Y/N")
            if again.lower() == "y":
                nati = -20
                thirst = 0
                miles = 0
                tired = 0
                canteen = 6
                continue
            elif again.lower() == "n":
                done == True
                break
            else:
                print("Not an Option")
    else:
        print("The Poachers Caught you!\nYou made it:",miles,"Miles")
        again = input("Would you like to play again?  Y/N")
        if again.lower() == "y":
            nati = -20
            thirst = 0
            miles = 0
            tired = 0
            canteen = 6
            continue
        elif again.lower()=="n":
            done == True
            break
        else:
            print("Not an Option")
print('Thanks for playing!')




