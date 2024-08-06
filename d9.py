def mult(v, m):   #矩阵相乘
    total = 0
    for i in range(len(v)):
        total += v[i]*m[i]
    return total

n = int(input())
weigh = list(map(int,input().split()))
dic = {}
for i in range(n):
    ls = list(input().split())
    dic[ls[0]] = list(map(int, ls[1:]))

sort = sorted(dic.items(), key=lambda x:(mult(x[1],weigh),x[0]), reverse=True)   #计算热度值并对其排序后还要对名字排序
    
for i in range(len(sort)):    
    print(sort[i][0])