import turtle
class MyOwnTurtle():
    def __init__(self,shape='turtle',color='black',size=2,position=(0,0)):
        self.tt = turtle.Turtle()
        self.tt.shape(shape)
        self.tt.shapesize(size,size)
        self.tt.color(color)
        self.tt.goto(position[0],position[1])


    def move_up(self):
        self.tt.setheading(90)
        self.tt.forward(100)

    def move_down(self):
        self.tt.setheading(270)
        self.tt.forward(100)
        
    def move_right(self):
        self.tt.setheading(0)
        self.tt.forward(100)

    def move_left(self):
        self.tt.setheading(180)
        self.tt.forward(100)