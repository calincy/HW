'''
描述
给定 n 个字符串，请对 n 个字符串按照字典序排列。

数据范围： 1<=n<=1000 , 字符串长度满足 1≤len≤100 

输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。

示例1
输入：
9
cap
to
cat
card
two
too
up
boat
boot

输出：
boat
boot
cap
card
cat
to
too
two
up
'''

while True:
    try:
        n = int(input())
        stack = []
        if 1 <= n <= 1000:
            for i in range(n):
                stack.append(input())
                if not 1<=len(stack[i])<=100:    #注意是 stack列表 第i个元素长度
                    break
                    
        print('\n'.join(sorted(stack)))

    except:
        break