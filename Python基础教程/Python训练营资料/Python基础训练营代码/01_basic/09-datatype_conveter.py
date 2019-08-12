# coding: utf-8

# 1. 为什么需要数据类型的转换
# math = raw_input(u'请输入数学成绩：'.encode('gbk'))
# english = raw_input(u'请输入英语成绩：'.encode('gbk'))

# # 'a' + 'b' = 'ab'
# # 其实math和english都是属于str数据类型
# # raw_input这个函数接受到的数据，都是字符串类型。
# # math + english并不是进行数学意义上的相加，而是进行字符串意义上的相加
# total = int(math) + int(english)

# print u'您的总分为：%s' % total



# 2. 转换成整形的方法是，使用int函数
# a  = 4.567
# b = int(a)
# print b

# a = '123abc'
# b = int(a)
# print b
# print type(b)

# a = 2147483648
# b = int(a)
# print type(b)

# 3. 转换成字符串的方法是，使用str函数
# 3.1 整形转换成字符串：
# a = 12
# b = str(a)
# print b
# print type(b)

# 3.2 浮点类型转换成字符串：
# a = 1.2
# b = str(a)
# print b
# print type(b)

# 3.3 长整形转换成字符串类型：
# a = 123L
# print a
# print type(a)
# print '=============='
# b = str(a)
# print b
# print type(b)

# 4. 其他三种数据类型转换成浮点类型，使用float函数
# 4.1 整形转成浮点类型
# a = 45
# b = float(a)

# print b
# print type(b)

# 4.2 字符串类型转成浮点类型
# a = "123.9"
# b = float(a)

# print b
# print type(b)

# 带有小数点的字符串，能不能转换成整形呢？
# 带有小数点的字符串  => 浮点类型   =>   整形
# a = "123.9"
# c = float(a)
# b = int(c)

# print b
# print type(b)

# 4.3 长整形转换成字符串类型
# a = 2147483648
# b = float(a)

# print b
# print type(b)

# 4. 其他三种数据类型转换成长整形，使用long函数
# 4.1 整形转换为长整形
# a = 123
# b = long(a)

# print a
# print type(a)
# print '=============='
# print b
# print type(b)

# 4.2 字符串类型转换为长整形
# 字符串转换为长整形，字符串中的字符都必须是数字，不能出现非数字
# a = '123.0'
# b = long(a)

# print a
# print type(a)
# print '=============='
# print b
# print type(b)

# 4.3 浮点类型转为长整形
a = 123.0
b = long(a)

print a
print type(a)
print '=============='
print b
print type(b)