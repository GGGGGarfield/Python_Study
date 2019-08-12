#coding: utf-8


PETS = []
ID = 0
FILE_NAME = 'pet_book.txt'

print(u"宠物寄养系统")
print(u"1. 添加新宠物")
print(u"2. 删除宠物")
print(u"3. 查找宠物")
print(u"4. 显示所有宠物")
print(u"5. 退出程序")


while True:
	value = raw_input(u'请输入操作序号：'.encode('gbk'))
	value = int(value)

	if value == 1:
		ID = raw_input(u'请输入宠物编号：'.encode('gbk'))
		pet_name = raw_input(u'请输入宠物名字：'.encode('gbk'))
		pet_type = raw_input(u'请输入宠物类型：'.encode('gbk'))
		pet_price = raw_input(u'请输入寄养价格：'.encode('gbk'))

		line = "{id}&{name}&{type}&{price}\n".format(id=ID,name=pet_name,type=pet_type,price=pet_price)
		with open(FILE_NAME,'a') as fp:
			fp.write(line)
		print u'恭喜！寄养成功！'
	elif value == 2:
		pet_id = raw_input(u"请输入宠物ID：".encode('gbk'))
		has_value = False
		for x in PETS:
			if int(pet_id) == x['id']:
				has_value = True
				PETS.remove(x)
				print u'删除成功！'
				break
		if not has_value:
			print u'没有该宠物'
	elif value == 3:
		pet_name = raw_input(u'请输入宠物名字：'.encode('gbk'))
		has_value = False
		for pet in PETS:
			if pet['name'] == pet_name:
				has_value = True
				print pet_name
				break
		if not has_value:
			print u'没有该宠物'

	elif value == 4:
		print u'id\tname\ttype\tprice'
		# for pet in PETS:
		# 	print "%s\t%s\t%s\t%s" % (pet['id'],pet['name'],pet['type'],pet['price'])
		with open(FILE_NAME,'r') as fp:
			# 1. read
			# 2. readline()
			# 3. readlines()
			# 4. 遍历fp文件对象
			for line in fp:
				infos = line.replace('\n','').split('&')
				print "%s\t%s\t%s\t%s" % (infos[0],infos[1],infos[2],infos[3])
	elif value == 5:
		break
	else:
		print u'您输入的有误，请重新输入！'