#coding: utf-8

num = 10


while True:
	value = raw_input(u'请输入您的值：'.encode('gbk'))
	value = int(value)
	if value > num:
		print u'太大了'
	elif value < num:
		print u'太小了'
	else:
		print u'恭喜您！答对啦！'
		break