# coding: utf-8

# 输入函数：用来接收用户输入的东西的
# username = raw_input(u'请您输入用户名：'.encode('gbk'))

# print username

# 输出函数：print函数。

# print 'hello world'

# username = 'zhiliao'
# # print username

# print 'my username is: %s' % username

username = raw_input(u'请输入您的用户名：'.encode('gbk'))
password = raw_input(u'请输入您的密码：'.encode('gbk'))

print u'您输入的用户名是：%s' % username
print u'您输入的密码是：%s' % password