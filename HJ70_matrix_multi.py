'''

描述

矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。

编写程序计算不同的计算顺序需要进行的乘法次数。

数据范围：矩阵个数：1≤n≤15,行列数：1≤row ,col≤100,保证给出的字符串表示的计算顺序唯一。

输入描述：
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
计算的法则为一个字符串，仅由左右括号和大写字母（'A'~'Z'）组成，保证括号是匹配的且输入合法！

输出描述：
输出需要进行的乘法次数

示例1
输入：
3
50 10
10 20
20 5
(A(BC))

输出：
3500

'''

while True:
    try:
        n = int(input())
        matrix_list = []
        for i in range(n):      #循环n个数量用range()
            matrix_list.append(list(map(int,input().split())))     #矩阵大小存储在二维数组中
        
        rule = input()
        stack = []      #栈，存储进行乘法运算的矩阵
        calcul = 0
        for i in rule:
            if i.isalpha():
                stack.append(matrix_list[ord(i)-65])
            if i == ')' and len(stack)>=2:
                b = stack.pop()
                a = stack.pop()
                calcul += b[1]*a[0]*a[1]
                stack.append([a[0],b[1]])
        print(calcul)
    except:
        break