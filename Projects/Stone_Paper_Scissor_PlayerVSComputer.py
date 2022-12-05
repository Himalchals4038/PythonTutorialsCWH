# Upgraded form of stone paper scissor with one player and computer.

import random

x = random.randint(1, 3)

if x == 1 :
    b = "st"
elif x == 2 :
    b = "p"
else :
    b = "sc"

a = input("Player Turn: ")
print("Computer Turn: ", b)

if a == "st" :
    if b == "p":
        print("b wins")
    elif b == "sc" :
        print("a wins")
    else :
        print("draw")
elif a == "p" :
    if b == "st" :
        print("a wins")
    elif b == "sc" :
        print("b wins")
    else :
        print("draw")
else :
    if b == "st" :
        print("b wins")
    elif b == "p" :
        print("a wins")
    else :
        print("draw")