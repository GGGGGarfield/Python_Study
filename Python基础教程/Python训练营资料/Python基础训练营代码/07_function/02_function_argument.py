#coding: utf-8

# def add(b,a):
# 	print a
# 	print b
# 	print a+b

# 1. 调用这个函数的时候，使用位置参数
# add(1,2)

# 2. 调用这个函数的时候，使用关键字参数
# add(a=1,b=2)
# 关键字参数传递一定要放在位置参数的后面
# add(2,a=1)

# 3. *args：arguments（缺省的位置参数）
# def add(a,b,*args):
# 	result = a+b
# 	# (3, 4, 5, 6)
# 	for x in args:
# 		result = result + x
# 	print result

# add(1,2,2,3,4)

# 4. **kwargs：缺省的关键字参数
# kwargs：keyword arguments
# def add(a,b,**kwargs):
# 	print a
# 	print b
# 	result = a + b
# 	if kwargs.get('is_print'):
# 		print result
# 	else:
# 		pass
# add(1,2)


# 5. 结合缺省的位置参数和缺省的关键字参数
# 注意点：
# 5.1. 缺省的位置参数和关键字参数必须要放在固定的参数后面
# 5.2. 关键字参数必须放在位置参数的后面（缺省的关键字参数也必须要在缺省
#  	 位置参数后面）
# def add(a,b,*args,**kwargs):
# 	print a
# 	print b
# 	print args
# 	print kwargs

# add(a=1,2)


# 6. *args和**kwargs可以囊括函数的所有的参数
# def add(*args,**kwargs):
# 	print args
# 	print kwargs

# add(1,2,a=1,b=2)


# 7. 将一个元组解包成位置参数传递进去
# 在调用这个函数的时候，可以将一个元组前面加一个*的语法
# 来将一个元组解包，然后将里面的值传递进去
# def add(a,b,*args):
# 	print a
# 	print b
# 	print args

# a_tuple = (1,2)
# # 以下代码等价于add(1,2)
# add(*a_tuple)

# 8. 将一个字典解包成关键字参数传递给函数
# def add(a,b,**kwargs):
# 	print kwargs

# add(1,2,**{'username':'zhiliao','age':18})

# 9. 默认参数
# 默认参数和缺省参数有一点不一样：
# 1. 默认参数即使用户不传递这个值，那么在函数中也可以使用这个变量。
# 	只不过这个变量的那个值是等于那个默认值而已。
# 2. 缺省参数，如果你没有传递值，那么就没有值。
# def add(a,b,c=0):
# 	print a+b+c

# add(9,11)

# 10. 所有类型的参数顺序总结：
# 10.1 普通的固定参数
# 10.2 带有默认值的参数
# 10.3 缺省的位置参数
# 10.4 缺省的关键字参数

# 普通参数 > 默认参数 > 缺省的位置参数 > 缺省的关键字参数

# def add(a,b=10,*args,**kwargs)