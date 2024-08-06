'''
描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
数据范围：字符串长度1≤s≤350 

输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度

示例1
输入：
cdabbacc

输出：
4

说明：
abba为最长的回文子串 
'''

while True:
    try:
        s = input()
        length = []

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:    #[::-1]表示字符串的逆序
                    length.append(j-i)        #s[i:j]是从s[i]到s[j-1]，不包s[j]，所以长度为j-i
        if length:
            print(max(length))

    except:
        break