# Exercise

# 在列表中，如果赋值b=a，改变b的某个序列值同样会改变a 
a = [3, 2, 1]
b = a
b[0] = 1
print(a)
print(b)

# 需要使用b=a[:]，这样修改b不会影响a
a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a)
print(b)


