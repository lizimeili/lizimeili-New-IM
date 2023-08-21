from random import randint



print("i        m         m")
print("         mm       mm")
print("i        m m     m m")
print("i        m  m   m  m")
print("i        m   m m   m")    


print("by:lizimeili")

while True:
    nemu = input("文本写入请输1,随机数请输2,退出请输3")
    nemu = int(nemu)
    if nemu == 1:
        data = input("写入内容")
        word0in = input("路径")
        ec = open(word0in,"w")
        ec.write(data)
        ec.close()
    elif nemu == 2:
        yok1 = input("开始边界")
        yok1 = int(yok1)
        yok2 = input("结尾边界")
        yok2 = int(yok2)
        ne = randint(yok1,yok2)
        print(ne)
    elif nemu ==3:
        break
