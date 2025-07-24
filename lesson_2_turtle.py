import turtle

colors = ['blue' , "red" , 'yellow']
while True:
    steps = int(input('please write steps you want to move'))
    what = input("what do you want ot make, square or circle")
    if what == "square":
        turtle.forward(steps)
        turtle.left(90)

        turtle.forward(steps)
        turtle.left(90)

        turtle.forward(steps)
        turtle.left(90)

        turtle.forward(steps)
        turtle.left(90)
    if what =='circle':
        turtle.circle(steps)


turtle.done()