import turtle
import random

wn = turtle.Screen()
wn.setup(width=600,height=1000)
wn.bgcolor("Black")
wn.title("Cross The Road")

colors = ["Red","Blue","White","Yellow","Seagreen","Orange"]


player = turtle.Turtle()
player.shape("triangle")
player.speed(0)
player.color("White")
player.shapesize(stretch_wid=2, stretch_len=2, outline=None)
player.up()
player.goto(0,-300)
player.speed(2)
player.left(90)

def randcolor():
    return colors[random.randint(0,5)]

obastacles = []
for i in range(10):
    obastacles.append(turtle.Turtle())
randy = 270
randx = -270
for car in obastacles:
    car.up()
    car.speed(0)
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
    car.color(randcolor())
    car.goto(randx,randy)
    randx += 160

randx = -270
obastacles2 = []
for i in range(10):
    obastacles2.append(turtle.Turtle())
randy2 = 200
for car in obastacles2:
    car.up()
    car.speed(0)
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
    car.color(randcolor())
    car.goto(randx,randy2)
    randx += 160

randx = -270
obastacles3 = []
for i in range(10):
    obastacles3.append(turtle.Turtle())
randy3 = 120
for car in obastacles3:
    car.up()
    car.speed(0)
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
    car.color(randcolor())
    car.goto(randx,randy3)
    randx += 160

randx = -270
obastacles4 = []
for i in range(10):
    obastacles4.append(turtle.Turtle())
randy4 = 20
for car in obastacles4:
    car.up()
    car.speed(0)
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
    car.color(randcolor())
    car.goto(randx,randy4)
    randx += 160

def move_up():
    player.fd(10)
def move_down():
    player.bk(10)

wn.listen()
wn.onkey(move_up,"Up")
wn.onkey(move_down,"Down")

collision = False

while collision == False:    
    for i in range(0,9):
        obastacles[i].fd(10)
        obastacles2[i].bk(10)
        obastacles3[i].fd(10)
        obastacles4[i].bk(10)
        car1 = obastacles[i].xcor()
        car2 = obastacles2[i].xcor()
        car3 = obastacles3[i].xcor()
        car4 = obastacles4[i].xcor()
        plpos = player.xcor()
        if (player.ycor() == randy) or (player.ycor() == randy2) or (player.ycor() == randy3) or (player.ycor() == randy4):
            if plpos - car1 <2 or plpos - car2 <2 or plpos -car3<2 or plpos-car4<2:
                print("Collison Happened")
                collision = True
            break