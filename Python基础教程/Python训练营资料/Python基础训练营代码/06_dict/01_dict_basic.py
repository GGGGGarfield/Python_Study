#coding: utf-8

# 创建字典的两种方式
# 1. 使用花括号的形式：用得比较多
# 列表：[1,2,3]
# 元组：()
# 第一种方式比较推荐
# person = {"username":"zhiliao",'age':'18'}

# 2. 使用函数的形式
# 关键字参数：xxx=xxx
# person = dict(username='zhiliao',age='18')

# 基本操作：
# 1. 求字典中有多少项键值对
# person = {"username":"zhiliao",'age':'18'}
# length = len(person)
# print(length)

# 2. 获取字典中，键对应的那个值
# 字典不能通过下标的形式进行操作，因为字典是无序的
# 字典中的键不能重复，因为如果重复了，那么后面给的键值对会把前面同名的键进行覆盖
# 如果通过方括号的形式访问一个字典中的key，但是这个key不存在，那么就会抛出一个异常，
# （连接上一行）如果你不想让他抛出异常，那么可以使用get方法
# person = {"username":"zhiliao",'age':'18','username':'ketang'}
# print(person)
# a = person['birthday']
# print(a)

# 3. 给字典添加值和修改值
# 如果这个字典中已经存在了这个key，那么就是修改
# 如果这个字典中不存在这个key，那么就是添加
# person = {"username":"zhiliao",'age':'18'}
# # person['height'] = 170
# person['username'] = 'ketang'
# print(person)

# 4. 删除字典中的一项
# person = {"username":"zhiliao",'age':'18'}
# del person['age']
# print(person)

# 5. k in d：用来检查字典中是否存在某个键值对
# person = {"username":"zhiliao",'age':'18'}
# if 'birthday' in person:
# 	print True
# else:
# 	print False

# 6. 字典的key可以有哪些值，value可以为任意数据类型
# 6.1. (浮点类型、整形、长整型)数值类型
# temp = {10L:'a',2:'b'}
# print temp

# 6.2. 字符串

# 6.3. 元组
# temp = {('a','b'):'12'}
# print temp

# 6.4. 列表：因为列表是可变的，所以不能当作字典的key
# temp = {['a','b']:'xxx'}
# print(temp)
