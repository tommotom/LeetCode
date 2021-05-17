class Solution:
    @lru_cache(None)
    def rearrangeSticks(self, n: int, k: int, mod=10**9+7) -> int:
        if k == 0: return 0
        if n == k: return 1
        return (self.rearrangeSticks(n-1, k-1) + (n-1) * self.rearrangeSticks(n-1, k)) % mod
