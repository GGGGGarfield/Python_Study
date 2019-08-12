#coding: utf-8

# apple = 'apple'
# banana = 'banna'
# orange = 'orange'

# fruits = ['apple',"banana",'orange']

# apple = fruits[0]
# banna = fruits[1]
# orange = fruits[2]

# print apple
# print banana
# print orange

# 遍历列表
# 1. for循环版本的遍历
# fruits = ['apple',"banana",'orange']
# # print type(fruits)
# for fruit in fruits:
# 	print fruit

# 2. while循环版本的遍历
# index = 0
# fruits = ['apple',"banana",'orange']
# length = len(fruits)
# while index < length:
# 	fruit = fruits[index]
# 	index += 1
# 	print fruit

# 列表嵌套
# test_list = [1,2,3,['a','b','c']]
# for x in test_list:
# 	if type(x) == list:
# 		for y in x:
# 			print y
# 	else:
# 		print x

# 列表相加
# a = [1,2,3]
# b = [3,4,5]
# c = a + b
# print c


# a = [1,2,3,4,5,6,7,8,9]

# temp = a[0:3]
# print temp

# temp = a[:]
# print temp

# temp = a[0::2]
# print temp

# 开始位置和结束位置其实也可以为负数
# 只不过如果是负数，那么最后一个元素是-1,一次类推
# temp = a[-3:]
# print temp

# [9,8,7]
# temp = a[-1:-4:-1]
# print temp

# temp = a[-1::-1]
# print temp


# 赋值
greet = ['hello','world']
greet[1] = 'zhiliao'
print greet
