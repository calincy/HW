'''
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

数据范围：字符串长度1≤length≤300 

输入描述：
输入两个字符串

输出描述：
返回重复出现的字符
示例1
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw

输出：
jklmnop
'''

while True:
    try:
        a = input()   #a保存较短串
        b = input()   #b保存较长串
        if len(a) > len(b):
            a,b = b,a
        result = ''

        for i in range(len(a)):
            for j in range(i+1,len(a)+1):
                if a[i:j] in b and j-i>len(result):
                    result = a[i:j]
        
        if result:
            print(result)
    
    except:
        break

