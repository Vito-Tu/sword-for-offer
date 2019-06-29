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
    """解法二：时间复杂度为O(nlogK)的算法，适合用来处理海量数据"""
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput) < k:
            return
        result = []
        for i in tinput:
            if len(result) < k:
                result.append(i)
            else:
                result.sort()
                if i < result[-1]:
                    result[-1] = i
        return sorted(result)
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
print(a.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 8))
                