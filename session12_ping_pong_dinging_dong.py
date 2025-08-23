import turtle

class Rod_ball(turtle.Turtle):
    def __init__(self, shape_parameter, color_p, size_x, size_y, position_x, position_y):
        super().__init__()
        self.shape(shape_parameter)
        self.color(color_p)
        self.shapesize(stretch_wid=size_y, stretch_len=size_x)
        self.penup()
        self.goto(position_x, position_y)

    def move_up(self):
        if self.ycor() < 380:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -380:
            self.goto(self.xcor(), self.ycor() - 20)


# Setup screen
screen = turtle.Screen()
screen.setup(width=1000, height=900)
screen.tracer(0)
screen.listen()

# Create rods and ball
right_Rod = Rod_ball("square", "red", 1, 10, 400, 0)
left_Rod = Rod_ball("square", "green", 1, 10, -400, 0)
ball = Rod_ball("circle", "black", 1, 1, 0, 100)

movement_list = [False, False, False, False]  # up, down, up2, down2


# Key events
def pressed(position):
    movement_list[position] = True
    print('pressed',position)

def released(position):
    movement_list[position] = False
    print('key released',position)


screen.onkeypress(lambda: pressed(0), "w")      # Left rod up
screen.onkeypress(lambda: pressed(1), "s")      # Left rod down
screen.onkeypress(lambda: pressed(2), "Up")     # Right rod up
screen.onkeypress(lambda: pressed(3), "Down")   # Right rod down

screen.onkey(lambda: released(0), "w")
screen.onkey(lambda: released(1), "s")
screen.onkey(lambda: released(2), "Up")
screen.onkey(lambda: released(3), "Down")


# Move rods
def move():
    if movement_list[0]:
        left_Rod.move_up()
    if movement_list[1]:
        left_Rod.move_down()
    if movement_list[2]:
        right_Rod.move_up()
    if movement_list[3]:
        right_Rod.move_down()
    screen.update()
    screen.ontimer(move, 10)


# Move ball
ball_speed_x = 5
ball_speed_y = 5

def move_ball():
    global ball_speed_x, ball_speed_y
    ball.setx(ball.xcor() + ball_speed_x)
    ball.sety(ball.ycor() + ball_speed_y)

    # Bounce on top/bottom walls
    if ball.ycor() > 390 or ball.ycor() < -390:
        ball_speed_y *= -1

    # Bounce on rods
    if (ball.xcor() > 380 and right_Rod.ycor() - 50 < ball.ycor() < right_Rod.ycor() + 50) or \
       (ball.xcor() < -380 and left_Rod.ycor() - 50 < ball.ycor() < left_Rod.ycor() + 50):
        ball_speed_x *= -1

    screen.update()
    screen.ontimer(move_ball, 20)


# Run
move()
move_ball()
turtle.done()


