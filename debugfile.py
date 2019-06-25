class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def Serialize(self, root):
        """递归的前序遍历二叉树，遇空节点使用特殊字符代替"""
        result = []
        if root == None:
            result.append(None)
            return result
        result.append(root.val)
        result = result + (self.Serialize(root.left))
        result = result + (self.Serialize(root.right))
        return result

    def Deserialize(self, s):
        """递归的读取序列生成节点"""
        if not s:
            return None
        value = s.pop(0)
        pRoot = None
        if value:
            pRoot = TreeNode(value)
            pRoot.left = self.Deserialize(s)
            pRoot.right = self.Deserialize(s)
        return pRoot
# test code
pRoot = TreeNode(10)
pRoot.left = TreeNode(6)
pRoot.right = TreeNode(14)
pRoot.left.left = TreeNode(4)
pRoot.left.right = TreeNode(8)
pRoot.right.left = TreeNode(12)
pRoot.right.right = TreeNode(16)
a = Solution()
# pRoot = [4,6,7,5]
print(a.Convert(pRoot))
                