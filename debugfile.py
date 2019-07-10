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
    def InversePairs(self, data):
        pass
# test code
# pRoot = TreeNode(10)
# pRoot.left = TreeNode(6)
# pRoot.right = TreeNode(14)
# pRoot.left.left = TreeNode(4)
# pRoot.left.right = TreeNode(8)
# pRoot.right.left = TreeNode(12)
# pRoot.right.right = TreeNode(16)
a = Solution()
# pRoot = [4,6,7,5]
data = 'abaccdebff'
for i in range(len(data)):
    a.Insert(data[i])
    print(a.FirstAppearingOnce())