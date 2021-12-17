class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        max_len = 0
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    max_len = max(max_len, dp[row][col])
        return pow(max_len, 2)
