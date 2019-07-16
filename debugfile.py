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
    def Reverse(self,data, pBegin, pEnd):
        if not data:
            raise Exception("输入数据为空")
        while pBegin < pEnd and pEnd < len(data):
            temp = data[pBegin]
            data[pBegin] = data[pEnd]
            data[pEnd] = temp
            pBegin += 1
            pEnd -= 1
    def LeftRotateString(self, s, n):
        data = ''
        if s:
            length = len(s)
            if length > 0 and n > 0 and n < length:
                data = list(s)
                pFirstStart = 0
                pFirstEnd = n - 1
                pSecondStart = n
                pSecondEnd = length - 1
                self.Reverse(data, pFirstStart, pFirstEnd)
                self.Reverse(data, pSecondStart, pSecondEnd)
                self.Reverse(data, pFirstStart, pSecondEnd)
        return ''.join(data)
# test code
# pRoot = TreeNode(5)
# pRoot.left = TreeNode(3)
# pRoot.right = TreeNode(7)
# pRoot.left.left = TreeNode(2)
# pRoot.left.right = TreeNode(4)
# pRoot.right.left = TreeNode(6)
# pRoot.right.right = TreeNode(8)
a = Solution()
data = "I am a student."
print(a.ReverseSentence(data))