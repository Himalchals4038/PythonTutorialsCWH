a = int(input("Enter your highscore: "))

def game() :
    return a

score = game()
with open('highscore.txt') as f :
    hiscore = f.read()

if hiscore == ' ' :
    with open('highscore.txt', 'w') as f :
        f.write(str(score))

elif int(hiscore) < a :
    with open('highscore.txt', 'w') as f :
        f.write(str(score))

else :
    pass
    