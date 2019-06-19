class TreeNode:
    """创建链表类"""
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.m_data = []
        self.m_min = []
    def push(self, node):
        self.m_data.append(node)
        if len(self.m_min) == 0 or node < self.m_min[-1]:
            self.m_min.append(node)
        else:
            self.m_min.append(self.m_min[-1])
    def pop(self):
        if len(self.m_min) > 0 and len(self.m_data) > 0:
            self.m_data.pop(-1)
            self.m_min.pop(-1)
        else:
            assert Exception("data is empty")
    def top(self):
        return self.m_data[-1]
    def min(self):
        return self.m_min[-1]



                