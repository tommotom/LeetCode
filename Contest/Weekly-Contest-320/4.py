class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        primes = set(['2', '3', '5', '7'])

        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0

        ids = [0]
        for i in range(n-1):
            if s[i] not in primes and s[i+1] in primes:
                ids.append(i+1)
        m = len(ids)

        mod = 1000000007
        @lru_cache(None)
        def helper(i, rest):
            if rest == 1:
                return 1 if ids[i] + minLength - 1 <= n-1 else 0
            ret = 0
            for j in range(i+1, m-rest+2):
                if ids[j]-ids[i] >= minLength:
                    ret += helper(j, rest-1)
            return ret % mod

        return helper(0, k)
