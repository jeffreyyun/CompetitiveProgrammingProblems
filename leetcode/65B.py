class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        # Droplet falls at heights[K]
        # If can fall left, falls left
        W = len(heights)

        def checkLeft():
            new_place = K
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                if heights[i] < heights[K] and heights[i] < heights[new_place]:
                    new_place = i

            return new_place


        def checkRight():
            new_place = K
            for i in range(K+1, W):
                if heights[i] > heights[i-1]:
                    break
                if heights[i] < heights[K] and heights[i] < heights[new_place]:
                    new_place = i

            return new_place



        for i in range(V):
            new_place = checkLeft()
            if new_place != K:
                heights[new_place] += 1
            else:
                new_place = checkRight()
                if new_place != K:
                    heights[new_place] += 1
                else:
                    heights[K] += 1

        return heights