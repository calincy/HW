'''
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。

提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）
'''

n = int(input())   #读取键值对个数
tinydict = {}    #创建空字典

#动态字典
for line in range(n):  #循环n次，分别读取n行键值对
    try:
        line = input().split()   #按空格切片并返回一个列表
        key = int(line[0])
        value = int(line[1])
        tinydict[key] = tinydict.get(key,0) + value
    except:
        continue
    
for i in sorted(tinydict):
    print(i,tinydict[i])


