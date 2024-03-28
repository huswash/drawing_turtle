from turtle import *
import turtle

# Set up the screen
wn = Screen()
wn.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.pencolor("white")

# Function to draw a heart
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()  

heart()
t.ht()

# write some text
def txt(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color('White')
    style = ('Arial', 16, 'italic')
    t.write(message, font=style)

txt('I', (-68, 95))
txt('L', (-55, 95))
txt('O', (-42, 95))
txt('V', (-30, 95))
txt('E', (-14, 95))
txt('Y', (10, 95))
txt('O', (26, 95))
txt('U', (45, 95))

wn.mainloop()