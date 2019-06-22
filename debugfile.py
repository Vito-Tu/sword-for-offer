class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence[-1]
        i = 0
        while i < len(sequence) - 1:
            if sequence[i] > root:
                break
            i += 1
        # for i in range(len(sequence) - 1):
        #     if sequence[i] > root:
        #         break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
# test code
# pRoot = TreeNode(8)
# pRoot.left = TreeNode(6)
# pRoot.right = TreeNode(10)
# pRoot.left.left = TreeNode(5)
# pRoot.left.right = TreeNode(7)
# pRoot.right.left = TreeNode(9)
# pRoot.right.right = TreeNode(11)
a = Solution()
pRoot = [4,6,7,5]
print(a.VerifySquenceOfBST(pRoot))
                