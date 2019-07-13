class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        return nLeft + 1 if nLeft > nRight else nRight + 1
# test code
pRoot = TreeNode(5)
pRoot.left = TreeNode(3)
pRoot.right = TreeNode(7)
pRoot.left.left = TreeNode(2)
pRoot.left.right = TreeNode(4)
pRoot.right.left = TreeNode(6)
pRoot.right.right = TreeNode(8)
a = Solution()
data = [-3,-3,1,3,5]
print(a.TreeDepth(pRoot))