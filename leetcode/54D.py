class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # O(N^2) time, O(N) space
        ans = []
        heights = []
        for i, box in enumerate(positions):
            pos, side = box
            left, right = pos, pos+side-1
            h = 0
            for j in range(i):
                ex_left, ex_right = positions[j][0], positions[j][0]+positions[j][1]-1
                # compare to see if this block overlaps with L/R boundaries of existing blocks
                if ex_right < left or ex_left > right:
                    continue
                # finds height of block based on heights of overlapping blocks
                else:
                    h = max(h, heights[j])
            # update the heights for this block
            h += side
            heights.append(h)
            # add height to ans
            if len(ans) == 0:
                ans.append(h)
            else:
                ans.append(max(h,ans[-1]))
        return ans

    # Dictionary approach (faster)
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        heights = {}
        for pos, side in positions:
            # finds nearby positions, if any
            left, right = pos, pos+side-1
            # compare to see if this block overlaps with L/R boundaries of existing blocks
            nearby = [key for key in heights.keys() if not (key[1] < pos or key[0] > right)]
            # finds height of block based on heights of existing and overlapping blocks
            if len(nearby) > 0:
                h = max(heights[key] for key in nearby) + side
            else:
                h = side
            # update the heights for left and right boundaries
            heights[(pos,right)] = h
            # add height to ans
            if len(ans) == 0:
                ans.append(h)
            else:
                ans.append(max(h,ans[-1]))
        return ans


sol = Solution()

inp = [[2,1],[2,9],[1,8]]

ppp = sol.fallingSquares(inp)

print(ppp)