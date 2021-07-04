class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def endsInA(n):
            if n == 1: return 1
            return (endsInE(n-1) + endsInI(n-1) + endsInU(n-1)) % mod

        @lru_cache(None)
        def endsInE(n):
            if n == 1: return 1
            return (endsInA(n-1) + endsInI(n-1)) % mod

        @lru_cache(None)
        def endsInI(n):
            if n == 1: return 1
            return (endsInE(n-1) + endsInO(n-1)) % mod

        @lru_cache(None)
        def endsInO(n):
            if n == 1: return 1
            return endsInI(n-1) % mod

        @lru_cache(None)
        def endsInU(n):
            if n == 1: return 1
            return (endsInI(n-1) + endsInO(n-1)) % mod

        return (endsInA(n) + endsInE(n) + endsInI(n) + endsInO(n) + endsInU(n)) % mod
