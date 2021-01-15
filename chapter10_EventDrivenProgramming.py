#import turtle

#turtle.setup(400,500)

#wn = turtle.Screen()
#wn.title('mouse click')
#wn.bgcolor('pink')

#tess = turtle.Turtle()
#tess.color('orange')
#tess.pensize(3)
#tess.shape('circle')

#alex = turtle.Turtle()
#alex.color('blue')
#alex.forward(100)

# goes only once
#def h1():
#    tess.forward(100)
#    tess.left(56)

# wn.ontimer(h1,2000)

# goes
#def h1():
#    tess.forward(10)
#    tess.left(20)
#    wn.ontimer(h1,200)

#h1()
#wn.mainloop()


#def h2(x,y):
#    wn.title('got click at coords {0}, {1}'.format(x,y))
#    alex.right(84)
#    alex.forward(50)

#wn.onclick(h2)

# traffic light
import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title('Now Traffic Light!')
wn.bgcolor('pink')
tess = turtle.Turtle()

def draw_housing():
    tess.pensize(3)
    tess.color('darkgray','lightgrey')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
