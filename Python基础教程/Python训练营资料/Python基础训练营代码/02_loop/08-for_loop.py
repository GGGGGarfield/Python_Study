#coding: utf-8

# greet = 'hello world'

# for x in greet:
# 	print x

# greet = 'python papijiang papa mama'
# count = 0

# for x in greet:
# 	if x == 'p':
# 		count += 1

# print count

# 打印1-10之间的整数，如果碰到5，就退出整个循环

# range函数可以返回指定的从xx到xx之间的整数

# for x in range(1,11):
# 	if x == 5:
# 		break
# 	print x

# 打印1-10之间的整数，如果碰到5，就退出当前这一次循环
for x in range(1,11):
	if x == 5:
		continue
	print x
