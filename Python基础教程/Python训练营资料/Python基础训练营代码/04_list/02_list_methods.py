#coding: utf-8

# append在列表末尾添加元素
# a = [1,2]
# a.append(3)
# print a

# count
# a = ['to','be','or','not','to','be']
# result = a.count('to')
# print result

# extend：将一个列表中的元素添加到另一个列表中
# a = [1,2,3]
# b = [2,3,4]

# a.extend(b)
# print a

# index
# a = ['a','b','c','a']
# index = a.index('a')
# print index

# insert
# a = [2,3,4]
# a.insert(0,1)
# print a

# pop
# a = [1,2,3,4]
# temp = a.pop()
# print temp
# print a

# remove
# a = ['a','b','c','d','b']
# a.remove('b')
# print a

# reverse
# a = [1,2,3,4]
# a.reverse()
# print a
# b = a[-1::-1]
# print a
# print b

# sort：
# ascii:a-zA-Z
# 数字：负无穷-正无穷
# a = [4,3,5,1]
# a.sort()
# print a

# a = ['a','c','e','b']
# a.sort()
# print a
# a = [4,3,5,1]
# b = sorted(a)
# print a
# print b

# del：根据下标来删除元素
# a = ['a','b','c','d']
# del a[1]
# print a

# in：判断列表中是否存在某个元素
# a = ['a','b','c','d']
# if '1' in a:
# 	print True
# else:
# 	print False

# list函数：
a = 12
b = list(a)
print b