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
    def GetFirstK(self,data, k, start, end):
        if start > end:
            return -1
        middleIndex = (start + end) // 2
        middleData = data[middleIndex]
        if middleData == k:
            if (middleIndex > 0 and data[middleIndex - 1] != k) or middleIndex == 0:
                return middleIndex
            else:
                end = middleIndex - 1
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetFirstK(data, k, start, end)
    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        middleIndex = (start + end) // 2
        middleData = data[middleIndex]
        if middleData == k:
            if (middleIndex < len(data) - 1 and data[middleIndex + 1] != k) or middleIndex == len(data) - 1:
                return middleIndex
            else:
                start = middleIndex + 1
        elif middleData < k:
            start = middleIndex + 1
        else:
            end = middleIndex - 1
        return self.GetLastK(data, k, start, end)
    def GetNumberOfK(self, data, k):
        number = 0
        if data:
            first = self.GetFirstK(data, k, 0, len(data) - 1)
            last = self.GetLastK(data, k, 0, len(data) - 1)
            if first > -1 and last > -1:
                number = last - first + 1
        return number
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
data = [7,5,6,4]
print(a.InversePairs(data))
print(data)