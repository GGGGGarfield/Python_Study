if __name__ == "__main__":
    f = open("/code/Python-Basic/homework3.cfg", "r")
    s = f.readline()
    f.close()
    s = s.split(" ")
    print(type(s))
    print(s)