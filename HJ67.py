from itertools import permutations

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return float('inf')  # 避免除以零的情况
    return 0

def dfs(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                # 选出两个数字进行计算
                new_nums = []
                for k in range(len(nums)):
                    if k != i and k != j:     #排除已选出的两个数字num[i],num[j]
                        new_nums.append(nums[k])
                
                # 遍历所有运算符
                for op in ['+', '-', '*', '/']:
                    if op == '/' and nums[j] == 0:
                        continue
                    new_nums.append(calculate(nums[i], nums[j], op))
                    if dfs(new_nums):
                        return True
                    #在递归结束后（无论成功与否）移除刚才添加的结果，确保 new_nums 状态与之前保持一致。这就是所谓的回溯操作。
                    new_nums.pop()   
                    
    return False

def can_get_24(nums):
    # 获取所有排列组合
    for perm in permutations(nums):    #便利nums的所以可能排序
        if dfs(list(perm)):
            return True
    return False

# 读取输入
nums = list(map(int, input().split()))

# 输出结果
if can_get_24(nums):
    print("true")
else:
    print("false")
