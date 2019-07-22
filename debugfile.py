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
    def Add(self, num1, num2):
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry
        return num1
# test code
# pRoot = TreeNode(5)
# pRoot.left = TreeNode(3)
# pRoot.right = TreeNode(7)
# pRoot.left.left = TreeNode(2)
# pRoot.left.right = TreeNode(4)
# pRoot.right.left = TreeNode(6)
# pRoot.right.right = TreeNode(8)
a = Solution()
data = [9,11,8,5,7,12,16,14]
result = a.Add(5, 17)
print(result)