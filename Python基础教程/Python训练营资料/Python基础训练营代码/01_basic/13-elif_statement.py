# coding: utf-8

# 0：星期天
# 1-6：代表得是星期一到星期六

# else if/elif

index = raw_input(u'请输入星期数字：'.encode('gbk'))

index = int(index)

if index == 0:
	print u'星期天'
elif index == 1:
	print u'星期一'
elif index == 2:
	print u'星期二'
elif index == 3:
	print u'星期三'
elif index == 4:
	print u'星期四'
elif index == 5:
	print u'星期五'
# elif index == 6:
# 	print '星期六'
else:
	print u'星期六'
