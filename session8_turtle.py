from turtle_object import MyOwnTurtle
import turtle

t1 = MyOwnTurtle('turtle','red',5,(-300,0))
t2 = MyOwnTurtle('turtle','green',5,(-300,100))
t3 = MyOwnTurtle('turtle','blue',5,(-300,200))
t4 = MyOwnTurtle('turtle','yellow',5,(-300,-100))
t5 = MyOwnTurtle('turtle','black',5,(-300,-200))

turtle.listen()



turtle.onkeypress(t1.move_up,'w')
turtle.onkeypress(t1.move_down,'s')
turtle.onkeypress(t1.move_right,'d')
turtle.onkeypress(t1.move_left,'a')


turtle.onkeypress(t2.move_up,'Up')
turtle.onkeypress(t2.move_down,'Down')
turtle.onkeypress(t2.move_right,'Right')
turtle.onkeypress(t2.move_left,'Left')


turtle.onkeypress(t3.move_up,'i')
turtle.onkeypress(t3.move_down,'k')
turtle.onkeypress(t3.move_right,'l')
turtle.onkeypress(t3.move_left,'j')


turtle.done()


