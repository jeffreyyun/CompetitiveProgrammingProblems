class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix[0])):
            el = matrix[0][i]
            for j in range(min(len(matrix), len(matrix[0])-i)):
                if matrix[j][i+j] != el:
                    return False
        for i in range(len(matrix)):
            el = matrix[i][0]
            for j in range(min(len(matrix[0]), len(matrix)-i)):
                if matrix[i+j][j] != el:
                    return False
        return True






sol = Solution()
matrix = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
res = sol.isToeplitzMatrix(matrix)
for i in matrix:
    print(i)
print(res)
