'''
密码验证合格程序

密码要求:

1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）
'''

def check(s):
    
    if len(s) <= 8:
        return 0
    
    a,b,c,d = 0,0,0,0
    for item in s:
        if ord('a') <= ord(item) <= ord('z'):
            a = 1
        elif ord('A') <= ord(item) <= ord('Z'):
            b = 1
        elif ord('0') <= ord(item) <= ord('9'):
            c = 1
        else:             #不是前三种就视为其他符号
            d = 1        
    if a + b + c + d < 3:
        return 0
    
    for i in range(len(s)-2):
        if len(s.split(s[i:i+3])) >= 3:
            return 0
        
    return 1

while 1:
    try:
        print('OK' if check(input()) else 'NG')
    except:
        break