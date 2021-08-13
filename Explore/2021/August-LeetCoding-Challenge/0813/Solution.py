class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        c0 = any(matrix[i][0] == 0 for i in range(m))
        r0 = any(matrix[0][j] == 0 for j in range(n))

        for i, j in product(range(m), range(n)):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
        for i, j in product(range(1, m), range(1, n)):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if c0:
            for i in range(m):
                matrix[i][0] = 0
        if r0:
            for j in range(n):
                matrix[0][j] = 0
