#coding: utf-8

# del
# clear方法：用来清除字典中所有的键值对的
# person = {'username':'zhiliao','age':18}
# print(person)
# person.clear()
# print(person)

# 1. clear方法相关知识点补充
# python中，变量赋值，采用的是引用的方式
# person1 = {'username':'zhiliao','age':18}
# person2 = person1
# # person1 = {}
# person1.clear()

# print(person1)
# print(person2)

# 2. get方法：也是获取字典中某个键对应的那个值，但是和[]的形式不同的是
# 如果这个键不在字典中存在，那么不会抛出一个异常，而是返回一个默认值
# person = {'username':'zhiliao','age':18}
# # username = person.get('username')
# # print username
# birthday = person.get('birthday',0)
# print birthday

# 3. has_key： 其实跟k in d非常类似，只不过这个是个方法而已。
# 这个方法在python3中不存在了，所以还是推荐使用k in d的方式
# person = {'username':'zhiliao','age':18}
# if person.has_key('username'):
# 	print(True)
# else:
# 	print(False)

# 4. pop，从字典中，删除那个键对应的那个值
# 和del有区别的是，pop方法在执行完毕后，会将这个键对应的这个值返回回来
# person = {'username':'zhiliao','age':18}
# age = person.pop('age')
# print(person)
# print(age)

# 5. popitem
# person = {'username':'zhiliao','age':18}
# person.popitem()
# print person

# 6. update方法
person1 = {'username':'zhiliao','age':18}
person2 = {"heigh":180,'username':'ketang'}

person1.update(person2)
print person1