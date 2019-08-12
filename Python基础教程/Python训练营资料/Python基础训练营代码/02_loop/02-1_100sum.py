# coding: utf-8


# 求1-100的整数之和

# sum = 1+2+3+4...+99+100

# num = 1
# while  num <= 10:
# 	print num
# 	num = num + 1


# sum = 0

# sum = sum + 1

# sum = sum + 2

# sum = sum + 3
# # ...

# sum = sum + 100

sum = 0
index = 1
while index <= 100:
	sum = sum + index
	index = index + 1

# 5050
# 1+2+3,,,,+99+100
# 101*50 = 5050
print sum

