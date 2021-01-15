
# 根据输入的半径，计算圆的面积
r = float(input("What is your radius? "))
area = 3.1415926 * r * r
print(f"The area is {area}.")

# 2.14 Exercises
# 1
a = 'All'
b = 'work'
c = 'and'
d = 'no'
e = 'play'
f = 'makes'
g = 'Jack'
h = 'a'
i = 'dull'
j = 'boy.'
print(f"{a} {b} {c} {d} {e} {f} {g} {h} {i} {j}")

# 2
x_1 = 6 * 1 - 2
x_2 = 6 *( 1 - 2 )

# 3

# 4
bruce = 6
bruce = bruce + 4
print(bruce)

# 5
p  = 10000
n  = 12
r = 0.08
t = int(input("please enter your number of years: "))
amount = (1 + r/n) ** (n * t) * p
print(f"your final amount after {t} years is {amount}")

# 6
y_1 = 5 % 2
y_2 = 9 % 5
y_3 = 15 % 12
y_4 = 12 % 15
y_5 = 6 % 6
y_6 = 0 % 7
# y_7 = 7 % 0

# 7
go_off = (14 + 51) % 24
print(go_off)

# 8
current_time = int(input("What time is it now?(24h format) "))
wait_time = int(input("How many hours would you like to wait? "))
off_time = (current_time + wait_time) % 24
print(f"Your alarm will go off on {off_time} clock.")

# 3.1 Our first turtle program
#import turtle               #load "turtle" module
#wn = turtle.Screen()        #creat and open a window named wn
#alex = turtle.Turtle()      #creat a turtle named alex

#alex.forward(50)            #make alex move
#alex.left(90)
#alex.forward(30)

#wn.mainloop()               #keep a state where it waits for events

# 3.1 turtle attributes
#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#wn.title("Hi, Liu!")

#liu = turtle.Turtle()
#liu.color("yellow")
#liu.pensize(3)

#liu.forward(50)

#wn.mainloop()

# Practice 1/2/3
import turtle
wn = turtle.Screen()
p1 = turtle.Turtle()
bg_color = input("which background color you prefer to? ")
wn.bgcolor(f"{bg_color}")

p1_color = input("which tess's color you prefer to? ")
p1.color(f"{p1_color}")

p1_size = int(input("what is your tess's size? "))
p1.pensize(p1_size)

wn.mainloop()

# 3.8 Exercise
# 1
for i in range(5):
    print("I love U!")

# 2
for month in ["Jan.", "Feb.", "Mar."]:
    print(f"one of the months of the year is {month}.")