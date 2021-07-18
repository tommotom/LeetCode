class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [num for num in points[0]]

        for row in range(1, m):
            left = [-1] * n
            right = [-1] * n
            for col in range(n):
                left[col] = dp[col]
                if col > 0:
                    left[col] = max(left[col], left[col-1] - 1)
            for col in range(n-1, -1, -1):
                right[col] = dp[col]
                if col < n-1:
                    right[col] = max(right[col], right[col+1] - 1)
            for col in range(n):
                dp[col] = max(left[col], right[col]) + points[row][col]
        return max(dp)
