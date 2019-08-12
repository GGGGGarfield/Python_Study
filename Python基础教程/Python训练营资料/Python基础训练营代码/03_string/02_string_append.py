#coding: utf-8

# 采用+号的形式
# a = 'hello'
# b = 'world'

# c = a + ' ' + b
# print c

# 采用格式化的形式
a = "__"
b = 'name'

# "__name__"
# c = a + b + a
c = "%s%s%s" % (a,b,a)
print c