while True:
    a = 25
    guess = int(input("猜数游戏，请输入一个数字：\n"))
    if guess>a :
        print("猜大了\n")
    elif guess<a :
        print("猜小了\n")
    else:
        print("猜对了\n")
        break
