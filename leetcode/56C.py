class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        # Basic DP
        # Time: O(A*B)
        # Space: O(A)
        ans = 0

        memo = [[0 for i in range(len(A)+1)] for j in range(2)]
        row = 0
        # Memo basically records Longest Common Suffix -- only keeps last two rows
        for j in range(len(B)+1):
            row = not row
            for i in range(len(A)+1):
                # the init cells
                if i == 0 or j == 0:
                    memo[row][i] = 0
                # if equal
                elif A[i-1] == B[j-1]:
                    memo[row][i] = memo[not row][i-1] + 1
                    ans = max(memo[row][i], ans)
                # no common suffix
                else:
                    memo[row][i] = 0

        return ans

def printGrid(grid):
    for r in grid:
        print(r)
