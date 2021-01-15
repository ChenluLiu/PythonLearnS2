# calculate the distance between two points
def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = a**2 + b**2
    result = c ** 0.5
    return result

print(distance(2,2,1,1))

# Exercise 11
def compare(a,b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1

def test(x):
    if x:
        print("Correct")
    else:
        print("Failed")

test(compare(5,4) == 1)
test(compare(7,7) == 0)
test(compare(2,3) == -1)



