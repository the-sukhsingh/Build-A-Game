import turtle
import random

wn = turtle.Screen()
wn.setup(width=600,height=1000)
wn.bgcolor("Black")
wn.title("Turtle Race")

turtles = []

for i in range(6):
    turtles.append(turtle.Turtle())

colors = ["Red","Blue","White","Yellow","Seagreen","Orange"]


centerx = -270
upy = 270

for i in range(6):
    chotu = turtles[i]
    chotu.shape("turtle")
    chotu.color(colors[i])
    chotu.speed(0)
    chotu.up()
    chotu.goto(centerx,upy)
    chotu.shapesize(stretch_wid=2, stretch_len=2, outline=None)
    upy -= 80


def randomspeed():
    return random.randint(4,10)

winner = None

while winner == None:
    for chotu in turtles:

        chotu.fd(randomspeed())
        if chotu.xcor() >270:
            winner = chotu
            print("Winner is",chotu.color()[0])
        
    wn.update()