#coding: utf-8

# 我现在要打印1-10之间的整数，但是不要把5打印出来

# index = 0
# while index < 10:
# 	index += 1
# 	if index == 5:
# 		continue
# 	print index

# 打印1-10之间的所有奇数

index = 0
while index < 10:
	index += 1
	if index % 2 == 0:
		continue
	print index