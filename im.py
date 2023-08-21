from random import randint
import time


print("i        m         m")
print("         mm       mm")
print("i        m m     m m")
print("i        m  m   m  m")
print("i        m   m m   m")    


print("by:lizimeili")

while True:
    nemu = input("文本写入请输1,随机数请输2,游戏请输3,退出请输4")
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
        print("游戏")
        print("狗还是猫,1")
        print("随机钓鱼,2")
        print("????")
        game = input()
        game = int(game)
        
        if game == 1:
            amlit = randint(1,2)
            if amlit == 1:
                aml = "狗"
            if amlit == 2:
                aml = "猫"
            amlinpt = input("狗还是猫?")
            if amlinpt == aml:
                print("答对")
            else:
               print("不对")
        if game == 2:
            input("按回车丢鱼饵")
            print("等待三秒")
            time.sleep(3)   
            ne = randint(1,100)   
            if ne <=50:
                print("鱼跑走啦")
            if ne >51 and ne == 100:
                print("钓鱼成功")  
            