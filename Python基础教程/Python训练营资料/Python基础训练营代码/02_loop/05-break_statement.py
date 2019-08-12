#coding: utf-8

# break/continue只能在循环中使用，不能在其他地方使用，while、for循环中可以使用

num = 1
while num <= 10:
	print num
	if num == 5:
		break
	num += 1
