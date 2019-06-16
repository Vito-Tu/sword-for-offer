class ListNode:
    """创建链表类"""
    def __init__(self, x=None):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        """递归比较每一个节点的值，并将较小的节点加入新的链表中"""
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        pMergedHead = None
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1, pHead2.next)
        return pMergedHead


                