import turtle
import random

wn = turtle.Screen()
wn.setup(width=600,height=1000)
wn.bgcolor("Black")
wn.title("Ping Pong")


leftbar = turtle.Turtle()
leftbar.hideturtle()
leftbar.up()
leftbar.shape("square")
leftbar.goto(-290,0)
leftbar.shapesize(stretch_wid=2, stretch_len=4, outline=None)
leftbar.color("black")

rightbar = turtle.Turtle()
rightbar.hideturtle()
rightbar.up()
rightbar.shape("square")
rightbar.goto(290,0)
rightbar.shapesize(stretch_wid=2, stretch_len=4, outline=None)
leftbar.color("black")

ball = turtle.Turtle()
ball.up()
ball.goto(0)
ball.shape("circle")
ball.shapesize(stretch_wid=2, stretch_len=2, outline=None)
ball.color("white")
ball.speed(0)

def moveaup():
    if leftbar.ycor<400 and leftbar.ycor>-400:
        y = leftbar.ycor() + 10
        leftbar.sety(y)
def movebup():
    if rightbar.ycor<400 and rightbar.ycor>-400:
        y = rightbar.ycor() + 10
        rightbar.sety(y)
def moveadw():
    if leftbar.ycor<400 and leftbar.ycor>-400:
        y = leftbar.ycor() - 10
        leftbar.sety(y)
def movebdw():
    if rightbar.ycor<400 and rightbar.ycor>-400:
        y = rightbar.ycor() - 10
        rightbar.sety(y)


wn.listen()
wn.onkey(moveaup,"w")
wn.onkey(moveadw,"s")
wn.onkey(movebup,"Up")
wn.onkey(movebdw,"Down")