class Solution:
    @lru_cache(None)
    def smallestValue(self, n: int) -> int:
        org = n
        primes = []
        for num in range(2, ceil(sqrt(n))+1):
            if num > n: break
            while n % num == 0:
                n //= num
                primes.append(num)

        if n > 1: primes.append(n)
        if len(primes) < 2: return org
        val = sum(primes)
        if org != val: val = min(val, self.smallestValue(val))
        return min(val, org)
