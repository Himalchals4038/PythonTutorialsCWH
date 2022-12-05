# Raw form of stone paper scissor game with both players.

print("You have to choose one out of Stone, Paper and Scissor.")
a = input("Player 1 Turn : ")
b = input("Player 2 Turn : ")

if a == "Stone" and b == "Scissor" :
    print("a Wins the Game !!")
if b == "Stone" and a == "Scissor" :
    print("b Wins the Game !!")
elif a == "Stone" and b == "Paper" :
    print("b Wins the Game !!")
elif b == "Stone" and a == "Paper" :
    print("a Wins the Game !!")
elif a == "Paper" and b == "Scissor" :
    print("b Wins the Game !!")
elif b == "Paper" and a == "Scissor" :
    print("a Wins the Game !!")
else :
    print("Draw, Please Try Again !!")
