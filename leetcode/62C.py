class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Another application of Bellman-Ford...
        # O(N^2)

        self.count = 0
        edges = []
        def getEdges(root):
            self.count += 1
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            if root.left:
                edges.append((root.val, root.left.val, 1))
                edges.append((root.left.val, root.val, 1))
                getEdges(root.left)
            if root.right:
                edges.append((root.val, root.right.val, 1))
                edges.append((root.right.val, root.val, 1))
                getEdges(root.right)

        INF = 9999999999
        N = 1001
        distance = [INF]*N
        leaves = []
        distance[0] = -1
        distance[k] = 0

        getEdges(root)

        for _ in range(self.count):
            for edge in edges:
                u, v, w = edge
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        best_dist = INF
        for leaf in leaves:
            if distance[leaf] < best_dist:
                best_dist = distance[leaf]
                best_leaf = leaf

        return best_leaf