#coding: utf-8

username = 'zhiliao'

# 1. 普通的
a = username[0:3]

# 2. 到最后一个
# b = username[0:]
liao = username[3:6]
liao = username[3:]

# 3. 负数代表从后面数
liao = username[-4:]
print liao

# 4. 步长
# 语法：string[开始位置:结束位置+1:步长]
numbers = '123456789'
# 默认步长为1
temp = numbers[0::1]
# 奇数
temp = numbers[0::2]
# print temp
# 偶数
temp = numbers[1::2]
# print temp

# 5. 步长为正数代表是从左到右。步长为负数，代表从右到左 
# 取789，但是要倒过来成987
temp = numbers[-1:-4:-1]
# print temp
# 将整个字符串倒序
temp = numbers[-1::-1]
print temp


# a = username[1]
# print a

# a = username[6]
# a = username[7]
# print a

# range(1,11)
# username[0:3]

# a = username[0:3]
# print a

# 如果要取到字符串的末尾，后面那个结束的位置保持为空
# temp = '123456789'
# a = temp[0:]
# print a

# 步长
# temp = '123456789'
# a = temp[0::2]
# print a


