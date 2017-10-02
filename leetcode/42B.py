class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        link = 0
        count = 0
        curr = -float("inf")
        # greedy algorithm, find valid chain with minimum end link
        while curr != float("inf"):
            link = float("inf")
            count += 1
            for p in pairs:
                if p[0] > curr: # valid chain
                    link = min(link, p[1])  # min end link
            curr = link
        return count-1  # extra invalid link on last pass