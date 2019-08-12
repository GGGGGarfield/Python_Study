#coding: utf-8

source = raw_input(u'请输入图片源地址：'.encode('gbk'))
dest = raw_input(u'请输入图片目标地址：'.encode('gbk'))


with open(source,'rb') as fp1:
	with open(dest,'wb') as fp2:
		fp2.write(fp1.read())

print(u'恭喜！图片复制完成！'.encode('gbk'))