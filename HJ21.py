while True:
    try:
        a = input()
        s = list(a)
        for i in range(len(s)):
            if 'a' <= s[i] <= 'c':
                s[i] = '2'
            elif 'd' <= s[i] <= 'f':
                s[i] = '3'
            elif 'g' <= s[i] <= 'i':
                s[i] = '4'
            elif 'j' <= s[i] <= 'l':
                s[i] = '5'
            elif 'm' <= s[i] <= 'o':
                s[i] = '6'
            elif 'p' <= s[i] <= 's':
                s[i] = '7'
            elif 't' <= s[i] <= 'v':
                s[i] = '8'
            elif 'w' <= s[i] <= 'z':
                s[i] = '9'
            elif 'A' <= s[i] <= 'Y':
                s[i] = chr(ord(s[i].lower())+1)
            elif s[i] == 'Z':
                s[i] = 'a'
        print(''.join(s))     #join()是字符串方法，要保证序列(s)中全部是字符串类型
    except:
        break

#可以将A-Z，a-z,0-9全部输入测试一下