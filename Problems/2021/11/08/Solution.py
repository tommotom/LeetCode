class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def n_to_m(n, m):
            if n >= m:
                return 1

            ret = 0
            for i in range(n, m+1):
                left = n_to_m(n, i-1)
                right = n_to_m(i+1, m)
                ret += left * right

            return ret

        return n_to_m(1, n)
