import turtle
import random

while True:
    turtle.forward(random.randint(1,100))
    turtle.left(random.randint(1,360))
    if turtle.xcor() >300:
        break 
    if turtle.ycor() >300:
        break

turtle.done()