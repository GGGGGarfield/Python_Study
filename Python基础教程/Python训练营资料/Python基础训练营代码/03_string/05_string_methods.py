#coding:utf-8

# find
# username = "hello zhiliao"
# index = username.find('world')
# if index > 0:
# 	print index
# else:
# 	print u'您要查找的字符串不存在'

# index
# username = 'hello zhiliao'
# index = username.index('zhiliao')
# index = username.index('world')
# print index

# len函数
# username = 'zhiliao'
# length = len(username)
# print(length)

# count
# username = 'zhiliao python python'
# temp = username.count('python')
# print(temp)

# replace
# username = 'zhiliao python python'
# new_username = username.replace('python','ketang')
# print(username)
# print(new_username)

# split
# ['1','2',3]
# ['zhiliao','python','ketang']
# username = 'zhiliao,python,ketang'
# username_list = username.split(',')
# print(username_list)

# startswith
# username = 'zhiliao ketang'
# result = username.startswith('ketang')
# print(result)
# url = 'xxxx://www.baidu.com/'
# result = url.startswith('http')
# if result:
# 	print u'这是一个网址'
# else:
# 	print u'这不是一个网址'

# endswith
# username = 'zhiliao ketang'
# result = username.endswith('xxx')
# print(result)
# jpg/png/gif
# file_name = 'xxx.js'
# if file_name.endswith('jpg') or file_name.endswith('gif') or file_name.endswith('png'):
# 	print u'这是一个图片文件'
# else:
# 	print u'这不是一个图片文件'

# lower
# username = 'ZHILIAO'
# username_lower = username.lower()
# print(username)
# print(username_lower)

# captcha_server = 'uF4D'
# captcha_user = 'uf4d'
# if captcha_server.lower() == captcha_user.lower():
# 	print u'验证码正确'
# else:
# 	print u'验证码错误'

# upper
# username = 'zhiliao'
# username_upper = username.upper()
# print username
# print username_upper

# username = '   zhiliao   '
# username_strip = username.strip()
# print len(username)
# print username_strip
# print len(username_strip)

# strip
# telephone = '   18899997777   '
# telephone_strip = telephone.strip()
# print len(telephone_strip)
# print telephone_strip

# lstrip
# telephone = '   188899997777'
# new_telephone = telephone.lstrip()
# print new_telephone

# username = '   zhiliao python   '
# new_username = username.replace(' ','')
# print new_username

# partition
# username = 'python zhiliao python zhiliao'
# username_tuple = username.partition('zhiliao')
# print(username_tuple)

# isalnum
# username = 'zhiliao_111'
# result = username.isalnum()
# print result

# isalpha
# usernmae = 'zhiliao__'
# result = usernmae.isalpha()
# print result

# isdigit
# username = '123a'
# result = username.isdigit()
# print result

# isspace
# username = '      1'
# result = username.isspace()
# print result

# %s/%d
# name = 'zhiliao'
# age = 18
# greet = 'my name is %s, my age is %d' % (name,age)

# 1. format函数最简单的使用方式
# name = 'zhiliao'
# age = 18
# greet = 'my name is {}, my age is {}'.format(name,age)
# print greet

# 2. format函数使用位置i参数的方式
# name = 'zhiliao'
# age = 18
# greet = 'my name is {0}, my username is {0}, my age is {1}'.format(name,age)
# print greet

# 3. 关键字参数xx=xxx
# name = 'zhiliao'
# age = 18
# greet = 'my name is {username}, my username is {username}, my age is {age}'.format(username=name,age=age)
# print greet

all_methods = dir(str)
print all_methods
