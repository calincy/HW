'''
给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。

提示:
1.vin.length == pre.length
2.pre 和 vin 均无重复元素
3.vin出现的元素均出现在 pre里
4.只需要返回根结点，系统会自动输出整颗树做答案对比

示例1
输入：
[1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]

返回值：
{1,2,3,4,#,5,6,#,7,#,#,8}

      1
    /   \
  2      3
 /      / \
4      5   6
 \        /
  7      8
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rebuild(pre,vin):
    if not pre or not vin:
        return 0
    root_val = pre[0]
    root = TreeNode(root_val)   #前序遍历的第一个值为根节点
    m = vin.index(root_val)     #根节点在中序遍历中的索引值
    root.left = rebuild(pre[1:m+1],vin[:m])
    root.right = rebuild(pre[m+1:],vin[m+1:])
    return root

def output_result(root):
    result = []
    if not root:
        return result
    s = [root]
    while s:    
        c = s.pop(0)
        if c:
            result.append(c.val)
            s.append(c.left)
            s.append(c.right)
        elif any(s):
            result.append('#')
    return result

while True:
    try:
        pre, vin = eval(input())
        root = rebuild(pre,vin)
        result = output_result(root)
        print('{' + ','.join(map(str,result)) + '}')
    except:
        break


'''
# 1. 定义二叉树节点类
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 2. 递归函数，根据前序遍历和中序遍历结果构建二叉树
def buildTree(preorder, inorder):
    # 如果前序遍历或中序遍历为空，返回 None，表示空节点
    if not preorder or not inorder:
        return None

    # 前序遍历的第一个元素为当前子树的根节点值
    root_val = preorder[0]
    # 创建当前节点
    root = TreeNode(root_val)

    # 在中序遍历中找到根节点的位置，根节点左侧为左子树的中序遍历，右侧为右子树的中序遍历
    root_index_inorder = inorder.index(root_val)

    # 递归构建左子树和右子树，注意切片操作
    root.left = buildTree(preorder[1:1+root_index_inorder], inorder[:root_index_inorder])
    root.right = buildTree(preorder[1+root_index_inorder:], inorder[root_index_inorder+1:])

    # 返回当前根节点
    return root

# 3. 辅助函数，以字符串形式打印整颗二叉树
def level_order_traversal(root):
    result = []  # 存储层序遍历的结果
    if not root:
        return result
    
    queue = [root]  # 使用队列进行层序遍历，初始时将根节点加入队列
    while queue:
        current_node = queue.pop(0)  # 取出当前队列中的第一个节点并赋值给current_node
        if current_node:
            result.append(current_node.value)  # 将当前节点的值加入结果列表
            # 将当前节点的左右子节点加入队列，如果为空则用None代替
            queue.append(current_node.left if current_node.left else None)
            queue.append(current_node.right if current_node.right else None)
        # 如果当前节点为空，并且队列中仍有节点，表示还二叉树没有遍历完，可将当前空节点输出为#；若所有节点已输出完，剩下的空节点不需要输出为#
        elif any(queue): 
            result.append('#')

    return result

# 4. 示例输入
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]

# 5. 构建二叉树
root = buildTree(preorder, inorder)

# 6. 打印结果
result = level_order_traversal(root)
print('{' + ','.join(map(str,result)) + '}')
'''
 
