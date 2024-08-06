while True:
    try:
        a = input()
        n = a[::-1]  #逆序
        arr = []
        for i in n:
            if i in arr:
                continue
            else:
                arr.append(i)
                print(i,end='')    #直接输出i，可不用调整格式,否则用 result=''.join(arr)
    except:
        break
