# coding: utf-8

# True/False

# a = True
# b = False

# print type(a)
# print type(b)

# if False:
# 	print 'success'
# else:
# 	print 'fail'

# print 'finished'

# a = 1
# b = 2
# if a == b:
# 	print 'equal'
# else:
# 	print 'not equal'

# username = raw_input(u'请输入用户名：'.encode('gbk'))

# if username == 'zhiliao':
# 	print u'恭喜！登录成功！'
# else:
# 	print u'抱歉，登录失败！'

# blacklist = 'zhiliao'

# username = raw_input(u'请输入用户名：'.encode('gbk'))
# if username != 'zhiliao':
# 	print u'您的用户是没有被加入到黑名单，可以正常使用'
# else:
# 	print u'您的用户被加入到黑名单，不能正常使用'

# if username == 'zhiliao':
# 	print u'您的用户被加入到黑名单，不能正常使用'
# else:
# 	print u'您的用户是没有被加入到黑名单，可以正常使用'

# age = 17
# if age > 17:
# 	print u'您可以进入到网吧了'
# else:
# 	print u'您年龄未满18岁，不能进入网吧'

# age = 17
# if age < 18:
# 	print u'您的年龄未满18岁，不能进入网吧'
# else:
# 	print u'您可以进入到网吧了'

# age = 18
# if age >= 18:
# 	print u'您可以进入到网吧了'
# else:
# 	print u'您的年龄未满18岁，不能进入网吧'

# age = 18
# if age <= 17:
# 	print u'您的年龄未满18岁，不能进入网吧'
# else:
# 	print u'您可以进入到网吧了'

# x and y
# 青年人的年龄划分：15-24

# age = raw_input(u'请您输入年龄：'.encode('gbk'))
# age = int(age)
# if age >= 15 and age <= 24:
# 	print u'您是一个青年人'
# else:
# 	print u'您不是一个青年人'


# age = raw_input(u'请您输入年龄：'.encode('gbk'))
# age = int(age)

# if age < 15 or age > 24:
# 	print u'您不是一个青年人'
# else:
# 	print u'您是一个青年人'

person1 = u'中国人'
person2 = u'南非'

# if person1 == u'中国人':
# 	print u'可以上战舰'
# else:
# 	print u'不可以上战舰'

if not person2 == u'中国人':
	print u'不可以上战舰'
else:
	print u'可以上战舰'