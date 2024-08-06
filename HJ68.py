while True:
    try:
        n = int(input())    #组数
        s = int(input())   #排序方式
        if s == 1:
            way = False
        else:
            way = True
        dic = {}
        for i in range(n):
            #可能输入的数据不足n行。因此也可以使用元组，用append往里面添元素，而不用判断到range(n)是否都格式正确
            # ls = []
            # name, score = input().split()
            # ls.append((name,int(score)))
            line = input().split()
            if len(line) != 2:      
                continue
            key = line[0]    
            value = int(line[1])   #易错点，要确保排序对象value是整数
            dic[key] = value
        reslist = sorted(dic.items(),key = lambda x:x[1], reverse = way)
        for x in reslist:
            print(*x)   # '*' 运算符用于解包（unpack）元组或列表的元素。
    except:
        break
