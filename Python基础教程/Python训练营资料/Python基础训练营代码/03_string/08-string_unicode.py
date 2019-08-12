#coding: utf-8

# pip install chardet
import chardet
import sys

name = u'知了'
# print name.encode('gbk')
# result = chardet.detect(name)
# print name
# print result

# gbk = cp936
# print sys.stdout.encoding



# unicode和utf-8编码的不同，以及为什么需要utf-8编码

# ord：用来将字母转换成ascii编码
# a => 97 => unicode
# a = ord('a')
# print bin(a)

# # print bin(ord('a'))
# 00000000 01100001

# # utf-8 
# 01100001

# str
# unicode
# a = u'xxx'
# print type(a)

# decode方法：用来将其他编码字符串转换成Unicode字符串
# a = 'xxx'
# # print chardet.detect(a)
# a_unicode = a.decode('ascii')
# print type(a_unicode)

# encode方法：用来将Unicoe字符串转换成其他编码的字符串
# a = u'中国'
# a_gbk = a.encode('gbk')
# print type(a_gbk)
# print a_gbk

# encode
# 商品(unicode) => (打包/encode) => 快递(经过编码后的str)

# decode
# 快递(经过编码后的str) => 解包(decode) => 商品(unicode)

# a = u'中国'
# print a

# 在raw_input函数中，即使提示文字是unicode字符串，也不会自动的将unicode
# 字符串转换为终端的编码。他会默认的转换为ascii编码。
# username = raw_input(u'请输入用户民：'.encode('gbk'))
# print username

# username = input('请输入用户名：')
# print(username)


# 在python2中，str到底使用什么编码，取决于字符串本身：
# 1. 如果你这个字符串本身都是ascii能够识别的字符，那么就采用ascii编码
# 2. 如果你这个字符串含有ascii编码不能识别的字符，那么就采用utf-8编码
# value = '中国'
# print chardet.detect(value)
# print value


# str：关注点，将unicode字符串转换为str类型的字符串
# str()函数，默认使用的是ascii编码进行编码。其实等价于string.encode('ascii')
# a = u'中国'

# # b = str(a)
# b = a.encode('utf-8')

# print type(a)
# print type(b)

# unicode：关注点，将str类型的字符串转换为unicode的字符串
# unicode()函数，默认使用的是ascii编码进行解码。其实等价于string.decode('ascii')
# a = '中国'
# # b = unicode(a)
# b = a.decode('utf-8')

# print type(a)
# print type(b)

# a = '中国' #str
# b = u'b' #unicode
# c = a.decode('utf-8') + b
# # c = unicode(a) + b
# print c
# print type(c)

# result = sys.getdefaultencoding()
# print result

reload(sys)
sys.setdefaultencoding('utf-8')

# str函数
# a = u'中国'
# b = str(a)
# print b

# unicode函数
# a = '中国'
# b = unicode(a)
# print b

# a = '中国'
# b = u'钓鱼岛'
# c = a + b
# print c

value = raw_input(u'请输入您的值：')
print value