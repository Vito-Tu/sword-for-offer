class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = [[]]
        levels = [[],[]]
        current = 0
        next = 1
        levels[current].append(pRoot)
        while levels[0] or levels[1]:
            pNode = levels[current].pop()
            result[-1].append(pNode.val)
            if current == 0:
                if pNode.left:
                    levels[next].append(pNode.left)
                if pNode.right:
                    levels[next].append(pNode.right)
            else:
                if pNode.right:
                    levels[next].append(pNode.right)
                if pNode.left:
                    levels[next].append(pNode.left)
            if not levels[current] and levels[next]:
                result.append([])
                current = 1 - current
                next = 1 - next
        return result
# test code
pRoot = TreeNode(8)
pRoot.left = TreeNode(6)
pRoot.right = TreeNode(10)
pRoot.left.left = TreeNode(5)
pRoot.left.right = TreeNode(7)
pRoot.right.left = TreeNode(9)
pRoot.right.right = TreeNode(11)
a = Solution()
print(a.Print(pRoot))
                