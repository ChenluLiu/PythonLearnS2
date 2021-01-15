# module random
import random
rng = random.Random()
dice_throw = rng.randrange(1,7)
delay_in_seconds = rng.random()
r_odd = rng.randrange(1,100,2)   # 1-99中的奇数（间隔2）
cards = list(range(52))  # int from 0 - 51
rng.shuffle(cards)    # 随机打乱顺序
print(cards)

def make_random_ints(num, lower, upper):
    rng = random.Random()
    result = []
    for i in range(num):
        result.append(rng.randrange(lower, upper))
    return result
list_a = make_random_ints(5,200,300)
print(list_a)

# module time
import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000
testdata = range(sz)
t0 = time.clock()
my_result = do_my_sum(testdata)
t1 = time.clock()
print('my_result    =   {0} (time taken = {1:.4f} seconds)'.format(my_result, t1-t0))

t2 = time.clock()
their_result = sum(testdata)
t3 = time.clock()
print('their_result    =   {0} (time taken = {1:.4f} seconds)'.format(their_result, t3-t2))

# module math
import math
pi = math.pi
print(pi)
e = math.e
print(e)
square = math.sqrt(2.0)
print(square)
radians = math.radians(90)    # 最好用radian来表示角度，而不是degree
print(radians)

# 变量的定义位置
n = 10
m = 3
def f(n):
    m = 7           #在函数内使用m=7
    return 2*n+m
print(f(5),n,m)     #在整体使用m=3

# module calendar
import calendar
cal = calendar.TextCalendar()
print(cal)
cal.pryear(2012)
print(cal)

# module copy
import copy
# 都有什么？能做什么？