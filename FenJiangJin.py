#分奖金
n=int(input())
lis = list(map(int, input().split()))
res=lis
for i in range(len(lis)):
    if i != len(lis)-1:
        for j in range(len(lis)-i-1):     #遇不到比自己数字大的，res内容不变：给自己分配随机数数量的奖金
        #for j in range(i,len(lis)):
            if lis[j+i+1]>lis[i]:
                res[i]=(j+1)*(lis[j+i+1]-lis[i])   #获得 距离 * 数字差值 的奖金
                break    #终止最深层的for循环
print(*res)
    