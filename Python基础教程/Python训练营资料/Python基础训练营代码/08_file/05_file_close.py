#coding: utf-8

# fp = open('xxx.txt','w')
# try:	
# 	fp.write('xxx')
# 	a = 1
# 	b = 0
# 	# c = a/b
# 	print'hello'
# except:
# 	print 'except'
# finally:
# 	print 'finally'
# 	fp.close()


with open('xxx.txt','w') as fp:
	fp.write('hello world')