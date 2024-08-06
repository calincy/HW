n = input()
s = []
res =[]
for i in n:
    s.append(ord(i))    #转化成ASCII码
s = sorted(s)    #排序
for i in s:
    res.append(chr(i))
print(''.join(res))