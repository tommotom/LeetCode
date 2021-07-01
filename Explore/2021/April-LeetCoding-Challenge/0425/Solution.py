class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            tmp = [x for x in matrix[i][i:n-i]]
            for r in range(n-i-1, i, -1):
                matrix[i][(n-1)-r] = matrix[r][i]
                matrix[r][i] = matrix[(n-1)-i][r]
                matrix[(n-1)-i][r] = matrix[(n-1)-r][(n-1)-i]
                matrix[(n-1)-r][(n-1)-i] = tmp[(n-1)-r-i]
