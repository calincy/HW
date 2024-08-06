import sys

class rect:
    def __init__(self):
        self.minrow = sys.maxsize
        self.maxrow = -sys.maxsize
        self.mincol = sys.maxsize
        self.maxcol = -sys.maxsize
    def setrow(self, row):
        self.maxrow = max(self.maxrow, row)
        self.minrow = min(self.minrow, row)
    def setcol(self, col):
        self.maxcol = max(self.maxcol, col)
        self.mincol = min(self.mincol, col)

m, n = map(int, input().split())
dic = {}

for i in range(m):    #遍历并更新最大最小行列值在字典中
    nums = list(map(int, input().split()))
    for j in range(n):
        num = nums[j]
        if num > 0:
            if num not in dic:
                dic[num] = rect()
            dic[num].setrow(i)
            dic[num].setcol(j)

maxsize = 0
for i in dic:
    num = dic[i]
    maxsize = max(maxsize, (num.maxrow-num.minrow+1)*(num.maxcol-num.mincol+1))
print(maxsize)


            





'''
import sys
 
class Rect:
    def __init__(self):
        self.minRow = sys.maxsize
        self.maxRow = -sys.maxsize
        self.minCol = sys.maxsize
        self.maxCol = -sys.maxsize
 
    def setRow(self, row):
        self.minRow = min(self.minRow, row)
        self.maxRow = max(self.maxRow, row)
 
    def setCol(self, col):
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)
 
# 输入获取
m, n = map(int, input().split())
 
rects = {}
 
for i in range(m):
    nums = list(map(int, input().split()))
    for j in range(n):
        num = nums[j]
 
        if num > 0: 
            if num not in rects:
                rects[num] = Rect()
            rects[num].setRow(i)
            rects[num].setCol(j)
 
maxArea = 0
for num in rects:
    rect = rects[num]
    maxArea = max(maxArea, (rect.maxRow - rect.minRow + 1) * (rect.maxCol - rect.minCol + 1))

print(maxArea)
'''