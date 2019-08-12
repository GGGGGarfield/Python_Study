#coding: utf-8

num = 10

value = raw_input(u'请输入您的值：'.encode('gbk'))

value = int(value)

while value != num:
	if value < num:
		print u'太小'
	elif value > num:
		print u'太大'

	value = raw_input(u'请输入您的值：'.encode('gbk'))

	value = int(value)

print u'恭喜您！答对了！'