#coding: utf-8

# 1. tell函数：获取当前文件指针所在的位置。
# fp = open('xxx.txt','r')
# string = fp.read(5)
# print(string)
# position = fp.tell()
# print position
# fp.close()

# 2. seek函数：改变文件指针的位置。
fp = open('xxx.txt','r')
# 2.1 from参数是0，表示以文件的开头为相对位置
# fp.seek(5,0)
# string = fp.read(5)
# print(string)
# 2.2 from参数位1，表示以当前位置为相对位置
# fp.seek(5,0)
# fp.seek(5,1)
# string = fp.read(7)
# print(string)
# 2.3 from参数为2，表示以文件末尾为相对位置
fp.seek(-8,2)
string = fp.read(6)
print(string)
fp.close()