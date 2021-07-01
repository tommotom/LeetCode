class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        nonPrimes = set([0, 1])
        for i in range(2, n+1):
            if i in nonPrimes: continue
            m = 2
            while i * m < n:
                nonPrimes.add(i * m)
                m += 1
        return n - len(nonPrimes)
