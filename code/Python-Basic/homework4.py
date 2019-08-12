"""
实现一个复制图片功能的系统：
用户输入图片的地址和名字，以及指定的图片。
"""

if __name__ == "__main__":
    path = input("please input file path:")
    name = input("please input file name:")
    try:
        fr = open(path+name, "rb")
        data = fr.read()
        try:
            fw = open(name, "wb")
            fw.write(data)
        except OSError:
            print("path is not available")
    except OSError:
        print("path is not available")
