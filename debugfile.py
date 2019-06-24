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
    # 返回 RandomListNode
    def CloneNodes(self,phead):
        """在原有的链表基础上进行赋值，即将每个节点沿着next链复制一个"""
        pNode = phead
        while pNode != None:
            pCloned = RandomListNode()
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pCloned.random = None
            pNode.next = pCloned
            pNode = pCloned.next
    def ConnetSiblingNodes(self, pHead):
        """修复复制后链表节点的random链接"""
        pNode = pHead
        while pNode != None:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next
            pNode = pClone.next
    def ReconnectNodes(self, pHead):
        """将复制好的链表拆分成两个链表，奇数位为原链表，偶数位为赋值好的链表"""
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode != None:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode != None:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead
    def Clone(self, pHead):
        self.CloneNodes(pHead)
        self.ConnetSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)
# test code
pRoot = TreeNode(8)
pRoot.left = TreeNode(6)
pRoot.right = TreeNode(10)
pRoot.left.left = TreeNode(5)
pRoot.left.right = TreeNode(7)
pRoot.right.left = TreeNode(9)
pRoot.right.right = TreeNode(11)
a = Solution()
# pRoot = [4,6,7,5]
print(a.FindPath(pRoot,27))
                