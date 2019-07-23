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
        self.g_nStatus = True
    def StrToInt(self, s):
        self.g_nStatus = False
        num = 0
        if s:
            minus = False
            i = 0
            if s[i] == '+':
                i += 1
            elif s[i] == '-':
                i += 1
                minus = True
            if i < len(s):
                num = self.StrToIntCore(s, i, minus)
        return int(num)
    def StrToIntCore(self, s, i, minus):
        num = 0
        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                flag = -1 if minus else 1
                num = num * 10 + flag * (ord(s[i]) - ord('0'))
                if (not minus and num > 0x7fffffff) or (minus and num < -0x80000000):
                    num = 0
                    break
                i += 1
            else:
                num = 0
                break
        if i == len(s):
            self.g_nStatus = True
        return num

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
print(a.StrToInt('-123'))