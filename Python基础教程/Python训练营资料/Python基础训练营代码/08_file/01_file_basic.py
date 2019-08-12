#coding: utf-8

# 1. 文件操作三部曲：
# 1.1. 以指定的方式，打开文件.
# 1.2. 做相关的操作（读数据、些数据）
# 1.3. 关闭文件
# fp = open('xxx.txt','r')
# fp.write('abc')
# fp.close()


# read方法
# fp = open('xxx.txt','r')
# string = fp.read()
# print(string)
# fp.close()

# write方法

# python2和python3默认打开文件的编码
# python2操作文件的时候，默认使用的是utf-8的编码
# python3操作文件的时候，如果没有指定编码，默认将使用系统自带的编码
# python3打开一个文件的时候，要指定文件的编码为utf-8
# fp = open('xxx.txt','w',encoding='utf-8')
# fp.write('中国')
# fp.close()

# r读方式打开文件，不能用于写入
# r：read
# fp = open('xxx.txt','r')
# string = fp.read()
# str(utf-8) => unicode => str(gbk)
# print string.decode('utf-8').encode('gbk')
# fp.write('知了')
# fp.close()

# w写方式打开文件，不能用于读
# w：write
# fp = open('xxx.txt','w')
# # fp.write('知了')
# string = fp.read()
# print(string)
# fp.close()

# a追加方式打开文件，不能用于读
# a：append
# fp = open('xxx.txt','a')
# # fp.write('中国')
# string = fp.read()
# print(string)
# fp.close()

# r+读写方式打开文件（基因）
# fp = open('xxx.txt',"r+")
# # string = fp.read()
# # print(string)
# fp.write('课堂')
# fp.close()


# w+读写方式打开文件（w的基因）
fp = open('xxx.txt','w+')
fp.write('hello')
fp.flush()
fp.seek(0,0)
string = fp.read()
print(string)
fp.close()


# a+追加和读的方式打开文件
fp = open('xxx.txt','a+')
# fp.write('zhiliao')
string = fp.read()
print(string)
fp.close()