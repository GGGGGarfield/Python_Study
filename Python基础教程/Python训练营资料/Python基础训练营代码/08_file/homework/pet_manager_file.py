#coding: utf-8

PETS_FILE_NAME = 'pets_book.txt'

print(u"宠物寄养系统")
print(u'0. 退出程序')
print(u"1. 添加新宠物")
print(u"2. 显示所有宠物")


while True:
	value = raw_input(u'请输入操作序号：'.encode('gbk'))
	value = int(value)

	if value == 1:
		ID = raw_input(u'请输入宠物编号：'.encode('gbk'))
		pet_name = raw_input(u'请输入宠物名字：'.encode('gbk'))
		pet_type = raw_input(u'请输入宠物类型：'.encode('gbk'))
		pet_price = raw_input(u'请输入寄养价格：'.encode('gbk'))

		with open(PETS_FILE_NAME,'a') as fp:
			fp.write('%s&%s&%s&%s\n'%(ID,pet_name,pet_type,pet_price))
		print u'恭喜！寄养成功！'
	elif value == 2:
		with open(PETS_FILE_NAME,'r') as fp:
			for line in fp:
				ID,name,pet_type,price = line.split('&')
				print("id:%s,name:%s,type:%s,price:%s"%(ID,name,pet_type,price))
	elif value == 0:
		break
	else:
		print u'您输入的有误，请重新输入！'
