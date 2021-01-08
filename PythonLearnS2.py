
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
import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

alex.forward(50)
alex.left(90)
alex.forward(30)

wn.mainloop()

