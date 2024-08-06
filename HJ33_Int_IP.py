'''
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成一个长整数。

举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序

输入：
10.0.3.193
167969729
输出：
167773121
10.3.3.193

'''


def BeInt(s):     #IP转为整数
    IPArr = s.split(".")
    binArr = str()   #创建一个新变量，并将其初始化为一个空字符串。
    
    if len(IPArr) == 4:
        for IP_item in IPArr:
            if 0 <= int(IP_item) <= 255:
                try:
                    bin_item = bin(int(IP_item))[2:]   #二进制前部的0会用0b代替，现去除0b才能正常转换为十进制
                    bin_item = '0'*(8-len(bin_item))+bin_item  #去掉的0b补为0   ;也可以使用zfill()
                    binArr += bin_item
                except:
                    return 0  
    
    return int(binArr,2)


def BeIP(s):    #整数转换成IP
    intArr = [0,0,0,0]
    IP = ''

    try:
        binary = '0'*(32-len(bin(int(s))[2:])) + bin(int(s))[2:]   #转成二进制时需将字符串转为整型
        intArr[0] = int(binary[0:8],2)
        intArr[1] = int(binary[8:16],2)
        intArr[2] = int(binary[16:24],2)
        intArr[3] = int(binary[24:],2)
    except:
        print("输入不合法")

    for int_item in intArr:
            IP += '.'+str(int_item)

    return IP[1:]


while True:     #无限循环，无限地处理用户输入
    try:
        ip = input()
        integer = input()
        print(BeInt(ip))
        print(BeIP(integer))
    except:
        break



''' 参考

while True:
    try:
        ip = input()
        num = input()
    except:
        break
    else:
        # ip to num
        ip_list = ip.split('.')
        ip2num = str()
        for i in ip_list:
            a = bin(int(i,10))[2:]
            a = '0'*(8-len(a)) + a if len(a)<8 else a
            ip2num += a
        print(int(ip2num,2))
        # num to ip
        num2ip = []
        num2 = bin(int(num,10))[2:]
        num2 = '0'*(32-len(num2)) + num2 if len(num2)<32 else num2
        for i in range(4):
            b = num2[8*i:8*i+8]
            b = str(int(b,2))
            num2ip.append(b)
        print('.'.join(num2ip))

'''




