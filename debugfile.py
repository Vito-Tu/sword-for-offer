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
    def __init__(self):
        self.data = []
        self.maximums = []
        self.currentIndex = 0
    def push_back(self, number):
        while self.maximums and number >= self.maximums[-1][0]:
            self.maximums.pop(-1)
        self.data.append([number, self.currentIndex])
        self.maximums.append([number, self.currentIndex])
        self.currentIndex += 1
    def pop_front(self):
        if not self.maximums:
            raise Exception('queue is empty')
        if self.maximums[0][1] == self.data[0][1]:
            self.maximums.pop(0)
        self.data.pop(0)
    def maxNumber(self):
        if not self.maximums:
            raise Exception("queue is empty")
        return self.maximums[0][0]
# test code
# pRoot = TreeNode(5)
# pRoot.left = TreeNode(3)
# pRoot.right = TreeNode(7)
# pRoot.left.left = TreeNode(2)
# pRoot.left.right = TreeNode(4)
# pRoot.right.left = TreeNode(6)
# pRoot.right.right = TreeNode(8)
a = Solution()
data = [2,3,4,2,6,2,5,1]
for i in data:
    a.push_back(i)
    print(a.maxNumber)
    if len(a.data) >= 3:
        a.pop_front()