#coding: utf-8

# 1. 局部变量：python会为函数单独开辟一块内存空间，这块空间外面是不能
# 访问的，所以里面定义的变量，外面同样也是不能访问的
# 那么在函数中定义的变量就是局部变量，只能在这个函数中使用

# 2. 全局变量：定义在python文件中，不属于任何代码块
# 全局变量可以在当前文件中所有的地方都可以用到
# age = 18
# def greet():
# 	username = 'zhiliao'
# 	print 'age:',age
# 	print 'username:',username

# greet()
# # print username
# print age


# 3. global关键字
# 定义变量
# USERNAME = 'zhiliao'
# # # 给变量重新赋值
# # USERNAME = 'xxx'

# def greet():
# 	# 1. 读全局变量没有问题
# 	# 2. 写（重新赋值）全局变量有问题吗
# 	# 在函数中，定义了一个和全局变量同名的变量，但是这个变量和全局
# 	# 变量是两个不同的变量，只不过名字恰巧相同而已。
# 	global USERNAME
# 	USERNAME = 'ketang'
# 	print 'i am %s' % USERNAME

# greet()
# print USERNAME


# 4. 可变数据类型当作全局变量来使用
PETS = []

def add_pet(pet):
	PETS.append(pet)
	print PETS

add_pet({'id':1,'name':'dimo','type':'dog'})

print PETS