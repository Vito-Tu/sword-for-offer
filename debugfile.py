class TreeNode:
    """创建链表类"""
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetricalCore(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalCore(pRoot1.left,pRoot2.right) and self.isSymmetricalCore(pRoot1.right, pRoot2.left)
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalCore(pRoot, pRoot)


                