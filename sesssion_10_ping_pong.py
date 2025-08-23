import turtle

def left_up(): left_rod.sety(left_rod.ycor()+50)
def left_down(): left_rod.sety(left_rod.ycor()-50)
def right_up(): right_rod.sety(right_rod.ycor()+50)
def right_down(): right_rod.sety(right_rod.ycor()-50)


win = turtle.Screen()
win.title('Ping pong with turtle')
win.bgcolor("green")
win.setup(1999,1080)
win.tracer(0)

left_rod = turtle.Turtle('square')
left_rod.shapesize(2,6)
left_rod.left(90)
left_rod.color('red')
left_rod.penup()
left_rod.goto(-900,0)


right_rod = turtle.Turtle('square')
right_rod.shapesize(2,6)
right_rod.left(90)
right_rod.penup()
right_rod.color('blue')
right_rod.goto(900,0)


ball = turtle.Turtle('circle')
ball.shapesize(2,2)
ball.penup()
ball.color("white")


win.listen()
win.onkeypress(left_up,'w')
win.onkeypress(left_down,'s')

win.onkeypress(right_up,'Up')

win.onkeypress(right_down,'Down')

x_position,y_position = 0,0
speed = 2
x_direction = speed

y_direction = speed
while True :
    x_position = x_position + x_direction
    y_position = y_position + y_direction
    
    ball.goto(x_position,y_position)
    if ball.ycor()>500:
        y_direction = -speed
    if ball.ycor()<-500:
        y_direction = speed
    if ball.xcor()>900:
        turtle.write('player 1 won',font=('Arial',40,'normal'))
        break
    if ball.xcor()<-900:
        turtle.write('player 2 won',font=('Arial',40,'normal'))
        break
    if ball.distance(left_rod)<50:
        x_direction = speed
    if ball.distance(right_rod)<50:
        x_direction = -speed





    win.update()



turtle.done()