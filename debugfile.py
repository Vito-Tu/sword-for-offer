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
    def beginNumber(self, digits):
        if digits == 1:
            return 0
        return pow(10, digits - 1)
    def digitsAtIndex(self,index, digits):
        number = self.beginNumber(digits) + index / digits
        indexFromRight = digits - index % digits
        for i in range(1,indexFromRight):
            number /= 10
        return int(number % 10)
    def countOfIntegers(self, digits):
        if digits == 1:
            return 10
        count = pow(10, digits - 1)
        return 9*count
    def digitsAtIndex_main(self, index):
        if index < 0:
            return -1
        digits = 1
        while True:
            number = self.countOfIntegers(digits)
            if index < number * digits:
                return self.digitsAtIndex(index, digits)
            index -= digits * number
            digits += 1
        return -1

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
data = -1
print(a.digitsAtIndex_main(data))