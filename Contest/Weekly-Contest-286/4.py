class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(i, n):
            if n == k: return 0
            if n > k or i == len(piles): return -float('inf')
            if i == len(piles) - 1:
                needed = k - n
                return -float('inf') if needed > len(piles[i]) else sum(piles[i][:needed])

            res, sum_i_j = -float('inf'), 0
            for j in range(len(piles[i])):
                sum_i_j += piles[i][j]
                tmp = sum_i_j + dp(i+1, n + j + 1)
                res = max(res, tmp)
            return max(res, dp(i+1, n))

        return dp(0, 0)
