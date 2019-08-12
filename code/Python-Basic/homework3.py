"""
实现一个宠物寄养管理系统，要求如下：
1. 需要使用函数来模块化。
2. 宠物的信息包括：宠物编号/宠物种类/宠物名字/宠物特色/一天的价格。
3. 需要实现：添加/查找/删除/修改/退出程序的功能。
4. 要求使用文件来存储信息，下次打开系统，数据依然存在。
"""
# Id Variety Name Characteristic Price
# Add Find Delete Modify Exit
petList = []

def addPet():
    pet = []
    pet.append(input("Id:")) 
    pet.append(input("Variety:"))
    pet.append(input("Name:"))
    pet.append(input("Characteristic:"))
    pet.append(input("Price:"))
    petList.append(pet)
    print("Done")

def deletePet():
    Id = input("Id:")
    for i in range(0, len(petList)):
        if Id == petList[i][0]:
            del petList[i]
            print("pet Id:", Id, "has been deleted")
            break
    
def findPet():
    print("filter: \n 0. Id \n 1. Variety \n 2. Name \n 3. Characteristic \n 4. Price")
    Prop = int(input("please select filter:"))
    Value = input("please input value:")
    for i in range(0, len(petList)):
        if Value == petList[i][Prop]:
            print("Id:", petList[i][0], end="  ")
            print("Variety:", petList[i][1], end="  ")
            print("Name:", petList[i][2], end="  ")
            print("Characteristic:", petList[i][3], end="  ")
            print("Price:", petList[i][4], end="\n")
    else:
        print("Done")

def modifyPet():
    Id = input("Id:")
    print("filter: \n 0. Id \n 1. Variety \n 2. Name \n 3. Characteristic \n 4. Price")
    Prop = int(input("please select filter:"))
    Value = input("please input value:")
    for i in range(0, len(petList)):
        if Id == petList[i][0]:
            petList[i][Prop] = Value

def exit():
    f = open("homework3.cfg", "w")
    for i in range(0, len(petList)):
        print(petList[i][0], petList[i][1], petList[i][2], petList[i][3], petList[i][4], file=f)
    f.close()

def init():
    f = open("homework3.cfg", "r")
    s = f.readlines()
    for i in range(0, len(s)):
        s[i] = s[i][0: len(s[i])-1]
        petList.append(s[i].split(" "))
    f.close()
    for i in range(0, len(petList)):
         print("Id:", petList[i][0], end="  ")
         print("Variety:", petList[i][1], end="  ")
         print("Name:", petList[i][2], end="  ")
         print("Characteristic:", petList[i][3], end="  ")
         print("Price:", petList[i][4], end="\n")

if __name__ == "__main__":
    init()
    while True:
        print(" 0. add a pet \n 1. delete a pet \n 2. find pets \n 3. modify pets \n 4. exit")
        sl = int(input("select:"))
        if 0 == sl:
            addPet()
        elif 1 == sl:
            deletePet()
        elif 2 == sl:
            findPet()
        elif 3 == sl:
            modifyPet()
        elif 4 == sl:
            exit()
            break
        else:
            print('error!')

