# coding: utf-8

###########Python2中raw_input和input的区别###############
# raw_input
# username = raw_input(u'请输入用户民：'.encode('gbk'))
# print username

# input函数：会把用户输入进来的字符串当成一个代码来执行
# username = input(u'请输入用户民：'.encode('gbk'))
# username = 1+2
# # username = zhiliao
# print username

# username = zhiliao
# print username


###############Python3中#####################
# 在Python3中只有一个输入函数，那就是input
# 只不过这个input函数等价于Python2中的raw_input函数

username = input('请输入用户民：')
print(username)