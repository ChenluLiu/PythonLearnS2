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

f = open('test.txt')    # 绝对地址："C:\\temp\\somefile.txt"   相对地址："/home/jimmy/somefile.txt"
content = f.read()
f.close()

words = content.split()
print(f"there are {len(words)} words in the file.")   # 为啥是9个？


# copy files from URL
import urllib.request

url = 'http://www.qingfan.com'
destination_filename = 'baidu.txt'

urllib.request.urlretrieve(url, destination_filename)
