# Upgraded form of stone paper scissor with both players.

print("You choose one out of Stone(st), Paper(p) and Scissor(sc).")

a = input("Player 1 Turn: ")
b = input("Player 2 Turn: ")

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
