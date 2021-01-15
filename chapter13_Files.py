myfile = open('test.txt','w')
myfile.write('my first file written from python\n')
myfile.write('---------------------------------\n')
myfile.write('Hello, world!\n')
myfile.close()

mynewhandle = open('test.txt','r')
while True:
    theline = mynewhandle.readline()
    if len(theline) == 0:
        break

    print(theline, end='')

mynewhandle.close()