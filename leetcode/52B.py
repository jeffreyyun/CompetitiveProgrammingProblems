# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.mx = 0

    def longestUnivaluePath(self, root, level=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        both = 0     # considers path covering both sides
        ret = 0     # returns longest branch on one side
        left = self.longestUnivaluePath(root.left, level+1)
        right = self.longestUnivaluePath(root.right, level+1)
        if root.left != None and root.val == root.left.val:
            both += left + 1
            ret = left + 1
        if root.right != None and root.val == root.right.val:
            both += right + 1
            ret = max(ret, right+1)
        self.mx = max(self.mx, both)
        if level > 0:
            return ret
        else:
            return self.mx

a1 = TreeNode(0)
a2 = TreeNode(4)
a3 = TreeNode(4)
a4 = TreeNode(4)
a5 = TreeNode(0)
a6 = TreeNode(0)

a1.left, a1.right = a2, a3
a2.left, a2.right = a4, a5
a5.left = a6

sol = Solution()
ppp = sol.longestUnivaluePath(a1)
print(ppp)
