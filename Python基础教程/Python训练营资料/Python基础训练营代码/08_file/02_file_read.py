#coding: utf-8

# 1. read函数
# read函数：
# fp = open('xxx.txt','r')
# string = fp.read(5)
# print(string)
# fp.close()

# readline函数：
# fp = open('xxx.txt','r')
# line1 = fp.readline()
# print(line1)
# line2 = fp.readline()
# print(line2)

# 2. readline函数：
# 用readline函数读取文件中所有的行数据
# 不能使用for循环去变量readline方法
# first_line = fp.readline()
# for line in first_line:
# 	print line

# 如果想用readline方法把文件中所有的行都读出来，只能采用while循环
# while True:
# 	line = fp.readline()
# 	if not line:
# 		break
# 	print(line)

# fp.close()



# 3. readlines函数：
# fp = open('xxx.txt','r')
# all_lines = fp.readlines()
# for line in all_lines:
# 	print line
# fp.close()

# 4. 遍历文件指针对象：
fp = open('big_file.txt','r')
# for line in fp:
# 	print(line)
# for line in fp.readlines():
# 	print line
for line in fp:
	print(line)

fp.close()
