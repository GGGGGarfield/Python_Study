#coding: utf-8

# 1. 遍历字典中所有的keys
# person = {'username':'zhiliao','age':18,'height': 180}

# for key in person.keys():
# 	print key

# 2. 也是遍历字典中所有的keys，但是使用的是iterkeys
# 如果字典内容比较多，那么推荐使用iterkeys，因为这个方法返回的是
# 一个迭代器，迭代器有一个优势，每次只会去取一个值，不会一次性把所有
# 的数据取出来，这样性能更高。
# person = {'username':'zhiliao','age':18,'height': 180}
# keys = person.keys()
# iterkeys = person.iterkeys()
# for key in person.iterkeys():
# 	print key

# 3. 使用values方法遍历所有的值
# person = {'username':'zhiliao','age':18,'height': 180}
# for value in person.values():
# 	print value
# for value in person.itervalues():
# 	print value
# values = person.values()
# itervalues = person.itervalues()
# print(values)
# print(itervalues)

# 4. 使用items方法遍历字典中所有的键和值
person = {'username':'zhiliao','age':18,'height': 180}
# items = person.items()
# for key,value in items:
# 	print key,value

# 5. 使用iteritems遍历字典中所有的键和值
# iteritems = person.iteritems()
for key,value in person.iteritems():
	print key,value


