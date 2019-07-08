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
    """定义一种新的比较大小数字大小的方法，使用该方法对数组进行排序，同时考虑大数问题"""
    def GetTranslationCount(self,number):
        if number < 0:
            return 0
        strNumber = str(number)
        length = len(strNumber)
        counts = [None] * length
        count = 0
        for i in range(length - 1, -1, -1):
            count = 0
            if i < length - 1:
                count = counts[i+1]
            else:
                count = 1
            if i < length - 1:
                digit1 = ord(strNumber[i]) - ord('0')
                digit2 = ord(strNumber[i+1]) - ord('0')
                converted = digit1 * 10 + digit2
                if converted >= 10 and converted <= 25:
                    if i < length - 2:
                        count += counts[i+2]
                    else:
                        count += 1
            counts[i] = count
        return count


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
data = 26
print(a.GetTranslationCount(data))