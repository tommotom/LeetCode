class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = defaultdict(int)
        for num in nums:
            while num % 2 == 0:
                factors[2] += 1
                num //= 2
            f = 3
            while f * f <= num:
                if num % f == 0:
                    factors[f] += 1
                    num //= f
                else:
                    f += 2
            if num != 1:
                factors[num] += 1
        return len(factors.keys())
