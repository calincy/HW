'''
描述
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。

数据范围：0≤m≤10 ，1≤n≤10 。

输入描述：
输入两个int整数

输出描述：
输出结果，int型

示例1
输入：
7 3

输出：
8
'''

def put(m,n):
    if m<0 or n<0:
        return 0
    if m==0:
        return 1
    if m==1 or n==1:
        return 1
    if m>1 and n>1:
        return put(m,n-1)+put(m-n,n)     #至少有一个空盘情况和每个盘子至少有一个苹果情况，两者为互斥事件，并集等于全集

while True:
    try:
        s = list(map(int,input().split(' ')))
        m = s[0]
        n = s[1]
        print(put(m,n))
    except:
        break