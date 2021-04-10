class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j):
            nonlocal matrix, r, c
            ans = 1
            if i > 0 and matrix[i][j] < matrix[i-1][j]: ans = max(ans, dfs(i-1, j)+1)
            if j > 0 and matrix[i][j] < matrix[i][j-1]: ans = max(ans, dfs(i, j-1)+1)
            if i+1 < r and matrix[i][j] < matrix[i+1][j]: ans = max(ans, dfs(i+1, j)+1)
            if j+1 < c and matrix[i][j] < matrix[i][j+1]: ans = max(ans, dfs(i, j+1)+1)
            return ans

        ans = 0
        for i in range(r):
            for j in range(c):
                ans = max(ans, dfs(i, j))
        return ans
