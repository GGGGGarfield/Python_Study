#coding: utf-8


# 第一种定义元组的方式
# a = 1,2,3
# print type(a)
# print a

# 第二种定义元组的方式
# a = (1,2,3)
# print a
# print type(a)

# 使用tuple函数定义远组
# a = [1,2,3]
# b = tuple(a)
# print b
# print type(b)

# 元组中只有一个元素的时候，要在这个元素的后面加一个逗号
# a = 1,
# print a
# print type(a)

# a = 'a','b','c'
# a[2] = 'd'

# a = 'zhiliao',18
# name,age = a

# print name
# print age

# a = 'zhiliao',18,'长沙'
# _,age,_ = a
# print age

# a = {'username':'zhiliao','age':18}
# print a
# print type(a)

# a_tuple = 'username',
# a_dict = {a_tuple:'zhiliao'}
# print a_dict

# a_list = ['username']
# a_dict = {a_list:'zhiliao'}
# print a_dict

def person():
	name = 'zhiliao'
	age = 18
	return name,age

a_tuple = person()
print a_tuple