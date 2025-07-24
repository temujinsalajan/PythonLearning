import turtle

screen = turtle.Screen()

temugn = turtle.Turtle()
umair = turtle.Turtle()
temugn.color('blue')
umair.color('red')
temugn.shape('turtle')


while True:
    x = input('where you want to move temugn?, left or right: ')
    if x == 'left':
        temugn.left(90)
        temugn.forward(100)
    elif x == "right":
        temugn.right(90)
        temugn.forward(100)






screen.mainloop()