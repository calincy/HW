'''
预订酒店

题目
放暑假了，小明决定到某旅游景点游玩，他在网上搜索到了各种价位的酒店（长度为 n 的数组 A），他的心理价位是 x 元，请帮他筛选出 k 个最接近 x 元的酒店（n>=k>0）,并由低到高打印酒店的价格。

输入
第一行：n, k, x
第二行：A[0] A[1] A[2]...A[n-1]

输出描述
从低到高打印筛选出的酒店价格
'''

n,k,x = map(int, input().split())
dic = {}    #key为酒店价格，item为差价
price = list(map(int, input().split()))   #酒店价格
for i in price:
    dic[i] = abs(i-x)
sort = sorted(dic.items(), key=lambda item:item[1])
rdic = dict(sort)   #重新转化为字典
rels = list(rdic.keys())   #只要输出酒店价格
sortls = sorted(rels[:5])
for i in range(k):
    print(sortls[i],end=' ')
