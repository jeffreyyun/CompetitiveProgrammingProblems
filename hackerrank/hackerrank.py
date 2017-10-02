#!/bin/python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        prefixSums = []
        self.getSums(root, sum, prefixSums)
        print(prefixSums)
        return self.count

    def getSums(self, root, sum, prefixSums=[]):
        if root == None:
            return
        elif root.val == None:
            prefixSums.append(0)
            return
        for i in range(len(prefixSums)):
            prefixSums[i] += root.val
            if prefixSums[i] == sum:
                print(prefixSums, sum)
                self.count += 1
            i = (i-1)//2
        if root.val == sum:                 # path with this node
            print(prefixSums, sum)
            self.count += 1
        prefixSums.append(root.val)         # path starting from this node
        self.getSums(root.left, sum, prefixSums)
        prefixSums.pop()
        self.getSums(root.right, sum, prefixSums)
        prefixSums.pop()
        return



values = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
nodes = [None for i in range(len(values))]
for i in range(len(values)):
    nodes[i] = TreeNode(values[i])
for i in range(len(values)//2):
    nodes[i].left = nodes[2*i+1]
    nodes[i].right = nodes[2*i+2]

sol = Solution()
ppp = sol.pathSum(nodes[0], 8)
print(ppp)