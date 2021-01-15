import turtle

wn = turtle.Screen()
wn.bgcolor("pink")

tess =turtle.Turtle()
tess.pencolor('black')
tess.pensize(5)
tess.shape("circle")

def keyr():
    tess.pencolor("red")

def keyg():
    tess.pencolor('green')

def keyb():
    tess.pencolor('blue')

def keyplus():
    x = int(tess.pensize)
    if x < 20:
        tess.pensize(x+1)
    else:
        tess.pensize(20)

def keyminus():
    x = int(tess.pensize)
    if x > 1:
        tess.pensize(x-1)
    else:
        tess.pensize(1)

wn.onkey(keyr,'r')
wn.onkey(keyg,'g')
wn.onkey(keyb,'b')
wn.onkey(keyplus, 'u')
wn.onkey(keyminus, 'd')

wn.listen()
wn.mainloop()

# 6
global scorea
global scoreb
global statenum
scorea = 0
socreb = 0

def score():
    # a wins
    if statenum == -1:
        scorea = scorea + 15
        statenum = 0
    # b wins
    elif statenum == 1:
        scoreb = scoreb + 15
        statenum = 0

while scorea < 65 or scoreb < 65:
    x = input('who wins this turn? ')
    if x == "a":
        statenum = -1
        score()
        print(f'the current score is: {scorea} vs {scoreb}')
    elif x == 'b':
        statenum = 1
        score()
        print(f'the current score is: {scorea} vs {scoreb}')
