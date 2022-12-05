class Remote :
    pass

class Player :
    def moveRight(self) :
        pass
    def moveLeft(self) :
        pass
    def moveTop(self) :
        pass
    
remote1 = Remote()
player1 = Player()

if (remote1.isLeftPressed()) :
    player1.moveLeft()
elif (remote1.isRightPressed()) :
    player1.moveRight()
elif (remote1.isTopPressed()) :
    player1.moveTop()
else :
    pass
