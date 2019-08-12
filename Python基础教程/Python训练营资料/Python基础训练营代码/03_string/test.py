#coding: utf-8
import chardet
import sys

reload(sys)
sys.setdefaultencoding('gbk')

# 1. str+unicode
# a = '中国'  # '中国'就不行了
# b = u'b'
# c = a + b
# print c

# str函数和unicode函数
# str函数：用来将其他数据类型转换为str类型字符串
# unicode函数：用来将其他数据类型转换为unicode字符串

# a = u'中国'
# b = str(a)
# c = a.encode('ascii')
# print b
# print c

# value = raw_input(u'请输入值：')
# print value


# str函数
# unicode函数
# str + unicode 的隐式转换
# sys.setdefaultencoding('utf-8')

reload(sys)
sys.setdefaultencoding('gbk')

# a = u'中国'
# b = str(a)
# print chardet.detect(b)
# print b

# a = '中国'
# b = unicode(a)
# print b

value = raw_input(u'请输入您的值：')
print value
