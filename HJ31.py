n = input()
#把所以非字母转换为空字符后直接用split
for i in n:
    if not ('a'<=i<='z' or 'A'<=i<='Z'):
    #if not i.isalpha():
        n = n.replace(i,' ')     
print(' '.join(n.split()[::-1]))