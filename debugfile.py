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
    def IsBalancedCroe(self, pRoot, pDepth):
        if not pRoot:
            pDepth[0] = 0
            return True
        left, right = [None], [None]
        if self.IsBalancedCroe(pRoot.left, left) and self.IsBalancedCroe(pRoot.right, right):
            diff = left - right
            if diff <= 1 and diff >= -1:
                pDepth[0] = 1 + (left[0] if left[0] > right[0] else right[0])
                return True
        return False
    def IsBalanced_Solution(self, pRoot):
        depth = [None]
        return self.IsBalancedCroe(pRoot, depth)
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