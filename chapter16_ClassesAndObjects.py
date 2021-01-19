class Point:
    'Point class represents and manipulates x,y coords.' # 注释会出现在调用时的说明中
    def __init__(self, x=0, y=0):
        'Create a new point at x, y' # 注释会出现在定义时
        self.x = x
        self.y = y

    def distance_from_origin(self):
        'Compute my distance from the origin'
        return((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return'({0}, {1})'.format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

class Rectangle:
    'A class to manufacture rectangle objects'
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
    
    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy


box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100,80),5,10)
print("box: ", box)
print("bomb: ", bomb)

box.width += 50
box.height += 100

r = Rectangle(Point(10,5), 100, 50)
print(r)
r.grow(25,-10)
print(r)
r.move(-10,10)
print(r)
