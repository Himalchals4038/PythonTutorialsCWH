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