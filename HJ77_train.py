'''
描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
要求输出所有火车出站的方案，以字典序排序输出。
数据范围：1≤n≤10 

输入描述：
第一行输入一个正整数N（0 < N <= 10），第二行包括N个正整数，范围为1到10。

输出描述：
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入：
3
1 2 3

输出：
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1

说明：
第一种方案：1进、1出、2进、2出、3进、3出
第二种方案：1进、1出、2进、3进、3出、2出
第三种方案：1进、2进、2出、1出、3进、3出
第四种方案：1进、2进、2出、3进、3出、1出
第五种方案：1进、2进、3进、3出、2出、1出
请注意，[3,1,2]这个序列是不可能实现的。   
'''

result = []

#建立递归函数处理遍历
def train_dfs(wait, stack, out):
    if not wait and not stack:
        result.append(' '.join(map(str,out)))
    if wait:      #入栈
        train_dfs(wait[1:], stack + [wait[0]], out)
    if stack:     #出栈
        train_dfs(wait, stack[:-1], out + [stack[-1]])

while True:
    try:
        n = input()
        num_train = list(map(int,input().split(' ')))
        train_dfs(num_train, [], [])
        for i in sorted(result):
            print(i)
    except:
        break




'''

res = []


# dfs 函数是递归函数，用于生成所有可能的出站序列。
# 它接受三个参数：
# wait 表示尚未入站的火车序列，
# stack 表示当前站台上的火车序列，
# out 表示已经出站的火车序列。

def dfs(wait, stack, out):      #wait、stack 和 out 都是列表（List）类型，每个列表的每个元素都是整数
    if not wait and not stack:
        res.append(' '.join(map(str, out)))    #如果 wait 和 stack 都为空，说明所有火车已经入站并出站，将当前出站序列添加到 res 中。
    if wait:      # 入栈  将wait的第一个元素去除，即第一个火车进站，stack+1:在站台末尾加入等待入站的第一个火车，即第一个火车移动到站台上。再对剩余等待入站的火车和新的站台状态进行递归调用
        dfs(wait[1:], stack + [wait[0]], out)  
    if stack:     # 出栈  去掉站台的最后一个火车，即让最后一个火车出站，已出站的火车队列末尾加上该火车
        dfs(wait, stack[:-1], out + [stack[-1]])   #只能将list连接到list

while True:
    try:
        n = int(input()),
        nums = list(map(int, input().split()))   #split()防止输入的内容包含空格而不能正常转换成int型错误
        dfs(nums, [], [])
        for i in sorted(res):    #sorted排序
            print(i)
    except:
        break

'''