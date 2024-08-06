#现在的兔子过两个月都会生一只：F(n+2)=F(n)+F(n-1)即F(n)=F(n-2)+F(n-1)——递归，并为斐波那契数列
n = int(input())   #月份
f = [0]*n
for i in range(n):
    if i < 2:
        f[i] = 1
    else:
        f[i] = f[i-2] + f[i-1]    #F(n)=F(n-2)+F(n-1)
print(f[n-1])

#函数
n = int(input())
def func(n):     
    if n<1:       #处理n=1时会出现f(-1)
        return 0
    elif 0<n<3:
        return 1
    else:
        return func(n-1)+func(n-2)    

print(func(n))