#coding: utf-8


# 1. 最基本的return返回值
# def add(a,b):
# 	result = a + b
# 	return result

# a = 1
# b = 2
# c = add(a,b)
# print c

# 2. return语句会影响代码的执行流程
# return语句执行完后，函数就相当于是结束，后面的语句就不会再执行了
# 一个函数中可以出现多个return语句，但是永远只会执行一个return语句
# def add(a,b):
# 	result = a + b
# 	if result > 10:
# 		return result

# 	print u'这个值是小于10的'
# 	return result

# c = add(1,20)

# 3. return语句一次性只能返回一个值
# 我们一般会使用元组来包装多个值进行返回

def greet():
	name = 'zhiliao'
	age = 18
	return name,age

a,b = greet()
print a
print b

