#coding: utf-8

# 1. sort函数回顾
# a = [3,4,522156,543,2,57,23]
# a.sort()
# print a

# 2. sort函数reverse参数
# a = [3,4,522156,543,2,57,23]
# a.sort(reverse=True)
# print a

# 3. sort函数key参数
# 函数也可以当作参数传递到其他函数中
# a = [{"username":"zhiliao",'age':18},{"username":'ketang',"age":20},{"username":'ketang',"age":21}]
# def sort_key(x):
# 	return x['age']
# a.sort(key=sort_key)
# print a

# 4. cmp函数:compare
# cmp(a,b)：函数需要传递两个参数：
#	1. 如果a>b，那么返回1
#	2. 如果a<b，那么返回-1
#	3. 如果a=b，那么返回0
# a = 2
# b = 2
# result = cmp(b,a)
# print result

# 5. sort函数cmp参数
# a = [{"username":"a",'age':18},{"username":'d',"age":20},{"username":'c',"age":20}]

# def sort_cmp(x,y):
# 	result = cmp(x['age'],y['age'])
# 	if result == 0:
# 		result = cmp(x['username'],y['username'])
# 		return result
# 	else:
# 		return result

# a.sort(cmp=sort_cmp)
# print a


# 6. lambda表达式实现key参数
# 如果一个函数只用到一次，并且代码特别少，那么建议使用lambda表达式来简化
# a = [{"username":"zhiliao",'age':18},{"username":'ketang',"age":20},{"username":'ketang',"age":21}]
# a.sort(key=lambda x:x['age'],reverse=True)
# print a

# 7. 自动动手写一个需要函数作为参数的函数
# 需求：要求两个值的一个运算（+、-、*、/）

def calculate(a,b,operate):
	a *= 10
	b *= 10
	result = operate(a,b)
	return result

a = 1
b = 2

c = calculate(a,b,lambda x,y:x+y)
print c

c = calculate(a,b,lambda x,y:x-y)
c = calculate(a,b,lambda x,y:x*y)
c = calculate(a,b,lambda x,y:x/y)