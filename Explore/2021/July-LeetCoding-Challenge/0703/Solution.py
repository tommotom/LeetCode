class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        cum = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cum[i][j] = matrix[i][j] + (cum[i][j-1] if j > 0 else 0)
        for i in range(1, m):
            for j in range(n):
                cum[i][j] += cum[i-1][j]

        ans = -float("inf")
        for end in range(m):
            for start in range(end+1):
                rest = []
                for col in range(n):
                    val = cum[end][col]
                    if start > 0:
                        val -= cum[start-1][col]
                    if val <= k:
                        ans = max(ans, val)
                    if rest:
                        idx = bisect.bisect_left(rest, val - k)
                        if idx < len(rest) and val - rest[idx] <= k:
                            ans = max(ans, val - rest[idx])
                    bisect.insort(rest, val)

        return ans
