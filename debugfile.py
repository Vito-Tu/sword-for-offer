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
    def NumberOf1(self,strN):
        """递归的计算含有1的数量"""
        if not strN:
            return 0
        first = ord(strN[0]) - ord('0')
        length = len(strN)
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1
        numFirstDigit = 0
        if first > 1:
            numFirstDigit = pow(10, length - 1)
        elif first == 1:
            numFirstDigit = int(''.join(strN[1:])) + 1
        numOtherDigts = first*(length - 1)*pow(10, length - 2)
        numRecursive = self.NumberOf1(strN[1:])
        return numFirstDigit + numOtherDigts + numRecursive
    def NumberOf1Between1AndN_Solution(self, n):
        if n <= 0:
            return 0
        return self.NumberOf1(list(str(n)))

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
data = [5,2,3,4,1,6,7,0,8]
for i in data:
    a.Insert(i)
    print(a.GetMedian())