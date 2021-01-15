import turtle

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

wn = make_window("pink","chapter_04")
a_1 = make_turtle("orange", 5)
a_2 = make_turtle("white", 2)

# Exercise 待补充