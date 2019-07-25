class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回对应char
    def __init__(self):
        self.data = []
        self.countNumber = [0]*256
        self.once = 0
    def FirstAppearingOnce(self):
        if not self.data:
            return '#'
        return self.data[self.once] if self.once < len(self.data) else '#'
    def Insert(self, char):
        self.data.append(char)
        self.countNumber[ord(char)] += 1
        while self.once < len(self.data) and self.countNumber[ord(self.data[self.once])] != 1:
            self.once += 1

# test code
# pRoot = TreeNode('a')
# pRoot.children.append(TreeNode('b'))
# pRoot.children.append(TreeNode('c'))
# temp = pRoot.children[0]
# temp.children.append(TreeNode('d'))
# temp.children.append(TreeNode('e'))
# temp = temp.children[0]
# temp.children.append(TreeNode('f'))
# temp.children.append(TreeNode('g'))
# temp = pRoot.children[0].children[1]
# temp.children.append(TreeNode('h'))
# temp.children.append(TreeNode('i'))
# temp.children.append(TreeNode('j'))
a = Solution()
data = 'google'
for i in range(len(data)):
    print('before insert the first appearing once char is ')
    print(a.FirstAppearingOnce())
    a.Insert(data[i])
    print('before insert the first appearing once char is ')
    print(a.FirstAppearingOnce())
    print('\n')