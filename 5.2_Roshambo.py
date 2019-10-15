'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
print("Welcoome to my ROSHAMBO program")
user_win=0
computer=0
ties=0
done=False
while done==False:
    quit=input("Would you like to quit?\n Y or N")
    if quit.lower()=="y":
        done=True
        break
    else:
        user=int(input("What is your choice?(Type in #)\n 1. Rock\n 2. Paper\n 3. Scissors"))
        if user==1:
            print("You chose Rock")
        elif user==2:
            print("You chose Paper")
        else:
            print("You chose Scissors")
        number=random.randrange(1,4)
        if number==user:
            print("It's a tie!")
            ties+=1
        elif number==1 and user==2:
            print("User Won!")
            user_win+=1
        elif number==1 and user==3:
            print("Computer Won!")
            computer+=1
        elif number==2 and user==1:
            print("Computer Won!")
            computer += 1
        elif number==2 and user==3:
            print("User Won!")
            user_win += 1
        elif number==3 and user==2:
            print("Computer Won!")
            computer += 1
        elif number==3 and user==1:
            print("User Won!")
            user_win+=1
print("BYE!")
print("Your Win/Loss/Tie record was\n",user_win,"/",computer,"/",ties)











