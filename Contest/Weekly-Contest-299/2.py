class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def helper(n):
            if n == 0: return 0
            if n == 1: return 2
            if n == 2: return 3
            return (helper(n-1) + helper(n-2)) % mod

        return (helper(n) * helper(n)) % mod
