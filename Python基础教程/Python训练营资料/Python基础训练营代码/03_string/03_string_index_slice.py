#coding: utf-8

# username = 'zhiliao'

# a = username[1]
# print a

# a = usrename[6]
# a = username[-1]
# a = username[7]
# print a

# range(开始位置,结束位置+1)
# string[开始位置:结束位置+1:步长]

# numbers = '123456789'
# numbers = 'zhiliao'
# temp = numbers[0:3]
# print temp

# 如果后面没有写，那么会一直取到最后面
# username = 'zhilia'
# temp = username[3:]
# print temp

# 索引值可以为负数，负数是从右到左边，最后一个数是-1
# username = 'zhiliao'
# temp = username[-4:]
# print temp

# 步长
numbers = '123456789'
# temp = numbers[0::2]
# print temp
# temp = numbers[1::2]
# print temp
# temp = numbers[0::1]
# print temp

# 步长为正数代表方向是从左到右。如果步长为负数，那么方向是从右到左
# temp = numbers[-1:-4:-1]
# print temp

# 将整个字符串进行倒序
temp = numbers[-1::-1]
print temp
