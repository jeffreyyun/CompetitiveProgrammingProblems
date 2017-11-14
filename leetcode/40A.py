class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        lev_sum = []
        lev_nodes = []
        avs = []

        def record(level, node):
            if level == len(lev_nodes):
                lev_nodes.append(0)
                lev_sum.append(0)
            lev_sum[level] += node.val
            lev_nodes[level] += 1
            if node.left:
                record(level + 1, node.left)
            if node.right:
                record(level + 1, node.right)

        record(0, root)
        for i in range(len(lev_nodes)):
            avs.append(lev_sum[i]/lev_nodes[i])

        return avs
