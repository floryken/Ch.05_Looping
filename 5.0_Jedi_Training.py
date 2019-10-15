  #Sign your name:Kenny Flory

'''
 1. Make the following program work.
   '''  
#print("This program takes three numbers and returns the sum.")
#total = 0
#for i in range(3):
 #   i = int(input("Enter a number: "))
  #  total+=i
#print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
#i=0
#for i in range(2,102,2):
 #   print(i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
#i=11
#while i<=11:
    #i-=1
    #if i==-1:
        #break
    #print(i)
#print("Blast Off!")
'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
#import random
#number=random.randrange(11)
#print(number)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total=0
pos=0
neg=0
zero=0
for i in range(7):
    i=int(input('Type a number: '))
    total+=i
    if i>0:
        pos+=1
    elif i==0:
        zero+=1
    else:
        neg+=1
print("Your total is ", total,"\nThere were ", pos,"psoitive, ",neg,"negative, and ",zero,"zeros.")
