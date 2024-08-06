n = input()
dic = {}   #创建字典
res = ''   #创建空字符串
for i in n:     #用字典算出每个变量出现次数
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1     #创建新键
mtimes = min(dic.values())    #字典中最小的值，即字符出现最少的次数
for i in n:
    if dic[i] != mtimes:
        res += i
#法二：空字符代替出现最少的字符
#     if dic[i] == mtimes:
#         n = n.replace(i,'')
# print(n)
print(res)