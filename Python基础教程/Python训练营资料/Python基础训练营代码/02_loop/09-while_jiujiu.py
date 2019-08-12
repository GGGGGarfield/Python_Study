#coding: utf-8

from __future__ import print_function

# 1. 总共有9行
# 2. 每行中的列数，就是当前所处的行号
# 3. 乘式的第一个数代表的是列，第二个数代表的是行

row = 1
column = 1

while row <= 9:
	while column <= row:
		print("%d*%d=%d" % (column,row,column*row),end=' ')
		column += 1
	print("")
	column = 1
	row += 1




# print语句的用法
# print("hello",end='')
# print("world")