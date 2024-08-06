while True:    #多行输入
    i = int(input())
    if i:
        result = 0
        while i//3:    #循环计算空瓶数，直到手里只剩<=2个空瓶
            result = result + i//3
            i = i//3 + i%3    #空瓶数
        if i == 2:
            result = result + 1 
        print(result,end='\n')
    elif not i:
        break

#最优解法
while True:
    n = int(input())
    if n == 0:
        break
    print(n//2)    #看最小单位，最少两个空瓶即可喝一瓶汽水，即每两个空瓶可喝一瓶汽水，除以2即可