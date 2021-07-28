class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        @lru_cache(None)
        def helper(n):
            if n == 1: return [1]
            odd = helper(n//2 + n%2)
            even = helper(n//2)
            return [2*o - 1 for o in odd] + [2*e for e in even]
        return helper(n)
