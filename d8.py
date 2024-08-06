def calculate_actual_prices(prices):
    n = len(prices)
    result = prices[:]  # 复制一份价格作为初始结果
    stack = []
    
    # 遍历价格数组两次以模拟循环效果
    for i in range(2 * n):
        current_price = prices[i % n]
        while stack and prices[stack[-1]] > current_price:   #执行完出栈操作后会继续循环与更前的值比较
            idx = stack.pop()
            result[idx] += current_price
        if i < n:
            stack.append(i)
    
    return result

# 读取输入
prices = list(map(int, input().split()))

# 计算结果
result = calculate_actual_prices(prices)

# 输出结果
print(" ".join(map(str, result)))
