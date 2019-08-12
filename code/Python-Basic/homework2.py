"""
用函数实现一个判断用户输入的年份是否是闰年的程序
1. 闰年是能被400整除
2. 或者是能被4整除但不能被100整除的数
"""
def isLeapYear(year):
    if 0 == int(year)%100:
        if 0 == int(year)%400:
            return True
        else:
            return False
    elif 0 == int(year)%4:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        try:
            year = int(input("please input the year:"))
            break
        except ValueError:
            print("this is not year")
    
    if True == isLeapYear(year):
        print(year, "is leap year")
    else:
        print(year, "is not leap year")