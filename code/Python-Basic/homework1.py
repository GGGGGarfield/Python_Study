""" 
使用while循环和for循环实现一个9*9乘法表
"""
for i in range(1,10):
    for j in range (1, i+1):
        print(j, "x", i, "=", i*j, sep="", end=" ")
    print("")