'''
Make a guess game where the system generates a random number between 1 and 500.
A user is given to guess that number. If he guesses more than the number, tell that it is more than the number.
If he guesses less than that number, tell that it is less than the number. 
If he guesses correct number then congratulate him. Also show him number of tries after which he was correct.
Also keep a record file where if the number of tries of user is less than the previous record, 
then update the file and display that the user has broken the previous record.
'''

from asyncore import loop
import random
a = random.randint(1,500)

print("The number is between 1 and 500")

for i in range (1, 500):
    b = int(input("Enter your guess: "))
    if a == b :
        print(f"You have made the perfect guess on {i}th try !!")
        break
    else :
        print("Try Again !!")
        if b > a :
            print("Your guessed number is more than actual number.")
        else:
            print("Your guessed number if less than actual number.")
    i += 1

with open('hiscore.txt', 'r') as f :
    hiscore = (f.read())

if i < int(hiscore) :
    print("You have just broken the previous guess record !!") 
    with open('hiscore.txt', 'w') as f :
        f.write(str(i))