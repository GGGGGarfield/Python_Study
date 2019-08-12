#coding: utf-8

def copy_image():
	source_file = raw_input(u'请输入源图片地址：'.encode('gbk'))
	dest_file = raw_input(u'请输入目标图片地址：'.encode('gbk'))
	with open(source_file,'rb') as fp1:
		with open(dest_file,'wb') as fp2:
			for x in fp1:
				fp2.write(x)

	print(u'恭喜！文件复制完成！')


copy_image()