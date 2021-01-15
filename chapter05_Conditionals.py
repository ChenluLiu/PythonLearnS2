# type "bool" --> True and False
a = (5 == (3 + 2))
print(a)
b = type(5 == (3 + 2))
print(b)

# and, or, not

# if elif else

# int() float() str()
print(int(2.6))
print(str(178))
print(float(1))

# turtle bar chart
import turtle

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(5)

#scale = [30, 50, 40, 80, 90]
#for v in scale:
#    draw_bar(tess, v)

#wn.mainloop()

# Exercise
# 1
input_num = input("please input a number: ")

def E1(a):
    if a == 0:
        print("Sunday")
    elif a == 1:
            print("Monday")
    elif a == 2:
        print("Tuesday")
    elif a == 3:
        print("Wedesday")
    elif a == 4:
        print("Thursday")
    elif a == 5:
        print("Friday")
    elif a == 6:
        print("Saturday")
    else:
        print("please input a number form 0 to 6")

start_num = input("please tell me your starting day number: ")
stay_num = input("please tell me your stay days: ")
total = start_num + stay_num
#day = total % 7
#E1(total)

# 6
def grade(score):
    if score >= 75:
        print(score, "scores makes you a First grade!")
    elif score >= 70:
        print(score, "scores makes you a Upper Second grade!")    
    elif score >= 60:
        print(score, "scores makes you a Second grade!")   
    elif score >= 50:
        print(score, "scores makes you a Third grade!")      
    else:
        print(score, "scores means you failed this time!")

xs = [83,75,74.9,70,69.9,65,55,45,40,2]

for x in xs:
    grade(x)

        