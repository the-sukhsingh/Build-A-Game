import turtle
import random
import time

delay = 0.1

t = turtle.Screen()
t.bgcolor("black")
t.title("snake game")
t.setup(height=600,width=600)
t.tracer()

head = turtle.Turtle()
head.shape("square")
head.color("red")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "back"

food= turtle.Turtle()
food.shape("square")
food.color("white")
food.speed(0)
food.goto(0,100)
food.penup()



def go_up():
    head.direction = "Up"
def go_down():
    head.direction = "Down"
def go_left():
    head.direction = "Left"
def go_right():
    head.direction = "Right"

def move():
    if head.direction("Up"):
        y= head.ycor()
        head.sety(y+20) 
    if head.direction("Down"):
        y = head.ycor()
        head.sety(y-20) 
    if head.direction("Left"):
        x = head.xcor()
        head.setx(x-20) 
    if head.direction("Right"):
        x = head.xcor()
        head.setx(x+20) 

t.listen()
t.onkeypress(go_up,"w")
t.onkeypress(go_down,"s")
t.onkeypress(go_left,"a")
t.onkeypress(go_right,"d")





while True:
    
    t.update()

    if  head.distance(food)<2 :
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

    move()


    time.sleep(delay)

   




    t.mainloop()