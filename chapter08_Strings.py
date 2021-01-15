fruit = 'banana'
print(list(enumerate(fruit)))
print(len(fruit))
length = len(fruit)
last = fruit[length-1]
print(last)

for i in range(6):
    print(fruit[i])

a = 0
while a < length:
    print(fruit[a])
    a += 1

for x in fruit:
    print(x)

# in, not in, find
def count_a(text):
    count = 0
    for c in text:
        if c == 'a':
            count += 1
    return(count)
print(count_a('banana'))

# split
a = "well I never did it"
b = a.split()
print(b)