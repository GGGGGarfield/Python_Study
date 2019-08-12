"""
函数式编程练习：
练习filter函数：使用filter函数过滤掉小于3的数：

 a = [1,2,3,4,5,6]

 # filter的用法：
 filter(函数,列表)
练习map函数：使用map函数将以下数组中所有的数都扩大10倍：

 a = [1,2,3,4,5,6]

 # map的用法
 map(函数,列表)
练习reduce函数：使用reduce函数求以下列表中数值之积：

 a = [1,2,3,4,5,6]

 # reduce函数用法
 reduce(函数,列表)

 # 比如求所有数值之和：
 b = a.reduce(lambda x,y:x+y,a)
"""
from functools import reduce

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    l = filter(lambda x: x>=3, a)
    l = list(l)
    print(l)

    l = map(lambda x: x*10, a)
    l = list(l)
    print(l)

    l = reduce(lambda x,y:x+y,a)
    print(l)