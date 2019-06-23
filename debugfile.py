class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPathCore(self,root, expectNumber, path, result):
        path.append(root.val)
        if sum(path) == expectNumber and (root.left == None and root.right == None):
            #找到一个匹配的路径
            result.append(path.copy())
        if root.left != None:
            self.FindPathCore(root.left,expectNumber,path, result)
        if root.right != None:
            self.FindPathCore(root.right,expectNumber,path,result)
        path.pop()
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        path = []
        result = []
        self.FindPathCore(root, expectNumber,path, result)
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
# pRoot = [4,6,7,5]
print(a.FindPath(pRoot,27))
                