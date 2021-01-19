class Point:
    'Point class represents and manipulates x,y coords.' # 注释会出现在调用时的说明中
    def __init__(self, x=0, y=0):
        'Create a new point at x, y' # 注释会出现在定义时
        self.x = x
        self.y = y

    def distance_from_origin(self):
        'Compute my distance from the origin'
        return((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return'({0}, {1})'.format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(4,2)
q = Point(6,3)

print(p.x, q.y)
print(q.distance_from_origin())

r = p.halfway(q)
print(r.to_string())

# exercise 6
class SMS_store:
    def __init__(self, has_been_viewed, from_number, time_arrived, text_of_SMS):
        self.has_been_viewed = 0
        self.from_number = '0'
        self.time_arrived = '0'
        self.text_of_SMS = ''


