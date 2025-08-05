import turtle

import random

score1 = 0
score2 = 0
apple=turtle.Turtle("circle")
apple.color('red')



t1 = turtle.Turtle('turtle')
t2 = turtle.Turtle('turtle')
t1.penup()
t2.penup()
apple.penup()


def make_square(tt):
    for i in range(4):
        tt.forward(100)
        tt.left(90)

def make_star(tt):
    for i in range(5):
        tt.forward(100)
        tt.left(144)


def check_coolion(tt):
    global score1, score2
    if tt.distance(apple)<20:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        apple.goto(x,y)
        if tt ==t1:
            score1 += 1
            print(f't1score{score1}')
        if tt == t2:
            score2 += 1
            print(f"t2score{score2}")
       

def up(tt):
    tt.setheading(270,90)
    tt.forward(10)
    check_coolion(tt)
    

def down(tt):
    tt.setheading(90,270)
    tt.forward(10)
    check_coolion(tt)

def left(tt):
    tt.setheading(180,360)
    tt.forward(10)
    check_coolion(tt)

def right(tt):
    tt.setheading(360,180)
    tt.forward(10)
    check_coolion(tt)




t1.color("blue")
t2.color("green")

turtle.listen()

turtle.onkeypress(lambda:up(t1),'Up')
turtle.onkeypress(lambda:down(t1),'Down')
turtle.onkeypress(lambda:left(t1),'Left')
turtle.onkeypress(lambda:right(t1),'Right')


turtle.onkeypress(lambda:up(t2),'w')
turtle.onkeypress(lambda:down(t2),'s')
turtle.onkeypress(lambda:left(t2),'a')
turtle.onkeypress(lambda:right(t2),'d')



turtle.done()

