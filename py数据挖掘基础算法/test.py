while True:
    a = int(input("摄氏转华氏输入1\n华氏转摄氏输入2\n"))
    if a == 2:
        degree1 = float(input("输入华氏温度"))
    #华氏摄氏转换 摄氏 ℃＝5/9（°F－32） 华氏°F＝ ℃×9/5＋32
        return1 = 5/9 * (degree1-32)
    #输出摄氏温度
        print("{:.2f}华氏度对应的摄氏温度是:{:.2f}".format(degree1,return1))

    elif a == 1:
        degree1 = float(input("输入摄氏温度"))
        return2 = (degree1)*(9/5)+32
        print("{:.2f}华氏度对应的摄氏温度是:{:.2f}".format(degree1,return2))
    else:
        break
