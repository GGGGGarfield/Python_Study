#coding: utf-8

# find
# username = 'zhiliao'
# subscript = username.rfind('i')
# print(subscript)

# index
# username = 'zhiliao'
# subscript = username.rindex('i')
# print(subscript)

# len
# username = 'zhiliao'
# print(len(username))

# count
# username = 'zhiliao python python'
# print(username.count('python'))

# replace
# username = 'zhiliao python python'
# print(username.replace('python','ketang'))

# split
# username = 'hello,i am zhiliao ketang'
# username_list = username.split(' ')
# print(username_list)

# startswith
# url = "http://www.baidu.com/"
# if url.startswith('http:'):
# 	print(True)
# else:
# 	print(False)

# endswith
# url = 'demo.py'
# print(url.endswith('py'))

# lower
# username = 'ZHILIAO'
# print(username.lower())

# upper
# username = 'zhiliao'
# print(username.upper())

# strip
# telephone = '  18877779999  '
# print(telephone.strip())

# lstrip
# telephone = '  18877779999  '
# print(telephone.lstrip())

# partition
# username = 'hello zhiliao world zhiliao'
# print(username.partition('zhiliao'))

# isalnum
# username = 'abc.123'
# print(username.isalnum())

# isalpha
# username = '123.123'
# print(username.isdigit())

# isspace
# username = ' '
# print(username.isspace())


# print(dir(unicode))

# person = {'name':'zhiliao','age':18}

# greet = "{} {}".format('hello','world')

# print greet

# # 1. 通过位置将参数格式化
# greet = "{0} {1}".format('hello','world')
# print greet

# # 2. 通过关键字参数格式化
# greet = "my name is {name}, my age is {age}".format(**{'name':'zhiliao','age':18})
# print greet

# # 3. 浮点数
# price = 'the apple price is {:.2f}'.format(18.234)
# print price
