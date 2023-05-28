class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        A = defaultdict(list)
        for i in range(m):
            for j in range(n):
                A[mat[i][j]].append((i, j))

        dp = [[0] * n for _ in range(m)]
        res = [0] * (m + n)
        for a in sorted(A):
            for i, j in A[a]:
                dp[i][j] = max(res[i], res[~j]) + 1
            for i, j in A[a]:
                res[i] = max(res[i], dp[i][j])
                res[~j] = max(res[~j], dp[i][j])

        return max(res)
