str1, str2 = input().split()
str = str1 + str2     #Step1

# odd_ls = []
# even_ls = []
# for i in range(len(str)//2):
#     odd_ls.append(str[2*i+1])   #奇数项
# for i in range(len(str)//2+len(str)%2):
#     even_ls.append(str[2*i])    #偶数项
# #奇偶数列分别排序
# odds = sorted(odd_ls)
# evens = sorted(even_ls)
# strs = [0]*len(str)   #用于存储排序后的字符串
# for i in range(len(odds)):
#     strs[2*i+1] = odds[i]
# for i in range(len(evens)):
#     strs[2*i] = evens[i]
#奇偶项排序简单方法
strs=list(str)
strs[::2] = sorted(strs[::2])
strs[1::2] = sorted(strs[1::2])

hex_str = []   #用于存储最终的十六进制大写
for i in strs:
    if ('0' <= i <= '9') or ('A' <= i <= 'F') or ('a' <= i <= 'f'):
        bin_str = bin(int(i,16))[2:].rjust(4,'0')[::-1]   #倒序后的二进制（4位）
        hex_str.append(hex(int(bin_str,2))[2:].upper())    #转换成十六进制大写,且仅保留数值部分（去掉0x）
    else:
        hex_str.append(i)
print(''.join(hex_str))