class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 1000000007
        @lru_cache(None)
        def dfs(pos, k):
            nonlocal endPos
            if k == 0:
                return 1 if pos == endPos else 0
            return (dfs(pos-1, k-1) + dfs(pos+1, k-1)) % mod
        return dfs(startPos, k) % mod
