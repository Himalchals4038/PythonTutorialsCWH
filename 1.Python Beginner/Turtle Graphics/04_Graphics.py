def drawSpiral(how_far,how_much):
    if how_far>0:
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','magenta','cyan'] 
        choice=random.choice(colors)
        t.pencolor(choice)
        t.forward(how_far)
        t.right(how_much)
        drawSpiral(how_far-5,how_much)

import turtle
import random
turtle.Screen().bgcolor("black")
t=turtle.Turtle() 
t.reset()
t.forward(2000)
t.pencolor('green')
t.pen(speed=10)
turtle.delay(10)
length = 500
turn_by =121
t.penup()
t.setpos(-length/2,length/2)
t.pendown()

drawSpiral(length,turn_by)