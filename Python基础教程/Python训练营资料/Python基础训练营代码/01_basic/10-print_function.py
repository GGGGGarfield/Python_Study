# coding: utf-8

# print 'abc'

# 整形（长整形）：%d
# 字符串类型：%s
# 浮点类型

# 字符串变量类型的格式化
# name = 'zhiliao'
# print 'my name is %s' % name

# 整形变量的格式化
# age = 2147483648
# print 'my age is %d' % age

# 浮点类型变量的格式化
# price = 18.9
# print "apple's price is %f" % price
# print "apple's price is %.f" % price

# name = 'zhiliao'
# age = 18
# gender = 'boy'
# # 元组
# print 'my name is %s,my age is %d,gender is %s' % (name,age,gender)

# 如果想字符串的末尾打印一个变量，那么可以采用以下方式
# age = 18
# print 'my age is',age

# 如果是其他数据类型，使用%s的方式进行格式化
# 那么其实，Python是首先将这个数据转换为字符串
# 再进行格式化。
# age = 18
# print 'my age is %s' % age

# python2版本
# print 'hello'
# 以上的形式，只能在Python2中使用。

# python3版本
# print('hello')
# 以上形式，既能在Python3中使用，也能在Python2中使用
age = 18
name = 'zhiliao'
print('my age is %d,my name is %s' % (age,name))
# print 'my age is %d' % age
