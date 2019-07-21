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
    def MaxDiff(self, numbers):
        if len(numbers) < 2:
            return 0
        min = numbers[0]
        maxDiff = numbers[1] - min
        for i in range(2, len(numbers)):
            if numbers[i-1] < min:
                min = numbers[i-1]
            currentDiff = numbers[i] - min
            if currentDiff > maxDiff:
                maxDiff = currentDiff
        return maxDiff
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
result = a.MaxDiff(data)
print(result)