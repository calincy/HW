'''
描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址从1.0.0.0到126.255.255.255;
B类地址从128.0.0.0到191.255.255.255;
C类地址从192.0.0.0到223.255.255.255;
D类地址从224.0.0.0到239.255.255.255;
E类地址从240.0.0.0到255.255.255.255

私网IP范围是：
从10.0.0.0到10.255.255.255
从172.16.0.0到172.31.255.255
从192.168.0.0到192.168.255.255

子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法子网掩码

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1
输入：
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0

输出：
1 0 1 0 0 2 1

说明：
10.70.44.68~255.254.255.0的子网掩码非法，19..0.~255.255.255.0的IP地址非法，所以错误IP地址或错误掩码的计数为2；
1.0.0.1~255.0.0.0是无误的A类地址；
192.168.0.2~255.255.255.0是无误的C类地址且是私有IP；
所以最终的结果为1 0 1 0 0 2 1        

示例2
输入：
0.201.56.50~255.255.111.255
127.201.56.50~255.255.111.255

输出：
0 0 0 0 0 0 0

说明：
类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略         
'''


count = {
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'error':0,
    'private':0
    }


def check_ip(ip):   #进来的ip为“1.12.1.3”形式
    ip_list = ip.split('.')
    if len(ip_list) != 4 or '' in ip_list:
        return 0
    for item in ip_list:
        if not 0 <= int(item) <= 255:
            return 0
    return 1

def check_mask(mask):
    if check_ip(mask):
        if mask == "0.0.0.0" or mask == "255.255.255.255":
            return 0
        mask_list = mask.split('.')
        mask_bin = ''
        for item in mask_list:
            item_bin = bin(int(item))[2:]
            mask_bin += item_bin.zfill(8)
        mask0 = mask_bin.find("0")
        mask1 = mask_bin.rfind("1")
        if mask1 == mask0 - 1:
            return 1
        else:
            return 0

def check_private_ip(ip):
    if check_ip(ip):
        ip_list = ip.split('.')
        first = ip_list[0]
        second = ip_list[1]
        if int(first) == 10:
            return 1
        if int(first) == 172:
            if 16 <= int(second) <= 31:
                return 1
        if int(first) == 192:
            if int(second) == 168:
                return 1
    return 0


while True:
    try:
        s = input()
        ip = s.split("~")[0]
        mask = s.split("~")[1]
        first = int(ip.split('.')[0])
        if first == 0 or first == 127:
            continue
        if check_ip(ip):
            if check_mask(mask):
                if 1 <= first < 127:
                    count['A'] += 1
                if 128 <= first < 192:
                    count['B'] += 1
                if 192 <= first < 224:
                    count['C'] += 1
                if 224 <= first < 240:
                    count['D'] += 1
                if 240 <= first <= 255:
                    count['E'] += 1
                if check_private_ip(ip):
                    count['private'] += 1
            else:
                count['error'] += 1
        else:
            count['error'] += 1
    except:
        break

for i in count.values():
    print(i,end=' ')


'''参考
ipClass2num = {
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'ERROR':0,
    'PRIVATE':0,
}
# 私有IP地址和A,B,C,D,E类地址是不冲突的，也就是说需要同时+1
def check_ip(ip:str):
    ip_bit = ip.split('.')
    if len(ip_bit) != 4 or '' in ip_bit:  #ip 的长度为4 且每一位不为空
        return False
    for i in ip_bit:
        if int(i)<0 or int(i) >255:   #检查Ip每一个10位的值范围为0~255
            return False
    return True
def check_mask(mask:str):
    if not check_ip(mask):
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        return False
    mask_list = mask.split('.')
    if len(mask_list) != 4:
        return False
    mask_bit = []
    for i in mask_list:#小数点隔开的每一数字段
        i = bin(int(i))#每一数字段转换为每一段的二进制数字段
        i = i[2:] #从每一段的二进制数字段的第三个数开始，因为前面有两个ob
        mask_bit.append(i.zfill(8)) #.zfill:返回指定长度的字符串，原字符串右对齐，前面填充0
    whole_mask = ''.join(mask_bit)
#     print(whole_mask)
    whole0_find = whole_mask.find("0")#查0从哪里开始
    whole1_rfind = whole_mask.rfind("1")#查1在哪里结束                   
    if whole1_rfind+1 == whole0_find:#两者位置差1位为正确
        return True
    else:
        return False
def check_private_ip(ip:str):
    # 三类私网
    ip_list = ip.split('.')
    if ip_list[0] == '10': return True
    if ip_list[0] == '172' and 16<=int(ip_list[1])<=31: return True
    if ip_list[0] == '192' and ip_list[1] == '168': return True
    return False
while True:
    try:
        s = input()
        ip = s.split('~')[0]
        mask = s.split('~')[1]
        if check_ip(ip):
            first = int(ip.split('.')[0])
            if first==127 or first==0:
                # 若不这样写，当类似于【0.*.*.*】和【127.*.*.*】的IP地址的子网掩码错误时，会额外计数
                continue
            if check_mask(mask):
                if check_private_ip(ip):
                    ipClass2num['PRIVATE'] += 1
                if 0<first<127: 
                    ipClass2num['A'] += 1
                elif 127<first<=191:
                    ipClass2num['B'] += 1
                elif 192<=first<=223:
                    ipClass2num['C'] += 1
                elif 224<=first<=239:
                    ipClass2num['D'] += 1
                elif 240<=first<=255:
                    ipClass2num['E'] += 1
            else:
                ipClass2num['ERROR'] += 1
        else:
            ipClass2num['ERROR'] += 1
    except:
        break
for v in ipClass2num.values():
    print(v,end=(' '))
'''