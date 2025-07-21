import turtle 

c1="grey"
steps=100
shape="turtle"
size=1


turtle.color(c1)
turtle.shape(shape)
turtle.shapesize(size)


while True:
    turtle.forward(steps)
    turtle.left(90)
    turtle.forward(steps)
    turtle.left(90)
    turtle.forward(steps)
    turtle.left(90)
    turtle.forward(steps)
    turtle.left(90)
    turtle.right(75)

turtle.done()

