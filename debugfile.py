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
    def PermutationCore(self, ss, i):
        result = []
        if i >= len(ss) - 1:
            result.append(''.join(ss))
            return result
        else:
            for j in range(i, len(ss)):
                if ss[j] == ss[i] and j != i:
                    # 防止输入中有重复字符
                    continue
                temp = ss[j]
                ss[j] = ss[i]
                ss[i] = temp
                result = result + self.PermutationCore(ss, i+1)
                temp = ss[j]
                ss[j] = ss[i]
                ss[i] = temp
        return result

    def Permutation(self, ss):
        if not ss:
            return ''
        return self.PermutationCore(list(ss), 0)
# test code
pRoot = TreeNode(10)
pRoot.left = TreeNode(6)
pRoot.right = TreeNode(14)
pRoot.left.left = TreeNode(4)
pRoot.left.right = TreeNode(8)
pRoot.right.left = TreeNode(12)
pRoot.right.right = TreeNode(16)
a = Solution()
# pRoot = [4,6,7,5]
print(a.Permutation('abc'))
                